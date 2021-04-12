import jwt
from django.conf import settings
from django.http import JsonResponse

from rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.kakao import views as kakao_views
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
import requests
from django.shortcuts import redirect
from .models import User

import urllib

# code 요청
def kakao_login(request):
    app_rest_api_key = settings.KAKAO_CID
    redirect_uri = f"http://{settings.DOMAIN}/account/login/kakao/callback/"
    redirect_url = f"https://kauth.kakao.com/oauth/authorize?client_id={app_rest_api_key}&" \
                   f"redirect_uri={redirect_uri}&response_type=code"
    return redirect(redirect_url)


class KakaoException(Exception):
    pass

# access token 요청
def kakao_callback(request):
    try:
        app_rest_api_key = settings.KAKAO_CID
        redirect_uri = f"http://{settings.DOMAIN}/account/login/kakao/callback/"
        user_token = request.GET.get("code")
        # post request
        token_request = requests.get(
            f"https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id={app_rest_api_key}&redirect_uri={redirect_uri}&code={user_token}"
        )
        token_response_json = token_request.json()
        error = token_response_json.get("error", None)

        # if there is an error from token_request
        if error is not None:
            raise KakaoException()
        access_token = token_response_json.get("access_token")

        # post request
        profile_request = requests.post(
            "https://kapi.kakao.com/v2/user/me",
            headers={"Authorization": f"Bearer {access_token}"},
        )
        profile_json = profile_request.json()

        # parsing profile json
        kakao_account = profile_json.get("kakao_account")

        email = kakao_account.get("email", None)
        kakao_id = profile_json.get("id")

        try:
            user_in_db = User.objects.get(email=email)
            # kakao계정 email이 서비스에 이미 따로 가입된 email 과 충돌한다면
            if user_in_db.register_login_method != User.REGISTER_LOGIN_KAKAO:
                raise KakaoException()

            data = {'code': user_token, 'access_token': access_token}
            accept = requests.post(
                f"http://127.0.0.1:8000/account/login/kakao/sociallogin/", data=data
            )
            accept_json = accept.json()
            accept_jwt = accept_json.get("token")

            # 프로필 정보 업데이트
            User.objects.filter(email=email).update(is_active=True)

        except User.DoesNotExist:
            # 서비스에 rest-auth 로그인
            data = {'code': user_token, 'access_token': access_token}
            accept = requests.post(
                f"http://127.0.0.1:8000/account/login/kakao/sociallogin", data=data
            )
            accept_json = accept.json()
            accept_jwt = accept_json.get("token")

            user = User.objects.create(
                email=email,
                register_login_method = User.REGISTER_LOGIN_KAKAO
            )
            user.set_unusable_password()
            user.save()


        return redirect("http://127.0.0.1:8000/")  # 메인 페이지

    except KakaoException:
        return redirect("http://127.0.0.1:8000/account/login")

class KaKaoSocialLoginView(SocialLoginView):
    adapter_class = kakao_views.KakaoOAuth2Adapter
    client_class = OAuth2Client
