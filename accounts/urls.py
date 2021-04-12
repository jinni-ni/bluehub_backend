from django.urls import path, include
from django.conf.urls import url

from allauth.account.views import confirm_email
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

from .views import kakao_login, kakao_callback, KaKaoSocialLoginView

app_name='account'

urlpatterns = [
    # 로그인
    path('', include('rest_auth.urls')),
    path('registration/', include('rest_auth.registration.urls')),
    path('', include('allauth.urls')),
    url(r'registration/confirm-email/(?P<key>.+)/$', confirm_email, name='confirm_email'),
    path('', include('django.contrib.auth.urls')),
    # 소셜 로그인
    path('login/kakao/', kakao_login, name='kakao_login'),
    path('login/kakao/callback/', kakao_callback, name='kakao_callback'),
    path('login/kakao/sociallogin/', KaKaoSocialLoginView.as_view(), name='kakao_social_login'),

    path('token/', obtain_jwt_token),
    path('token/refresh/', refresh_jwt_token),
    path('token/verify/', verify_jwt_token),
]
