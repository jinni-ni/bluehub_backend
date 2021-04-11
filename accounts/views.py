from django.shortcuts import redirect
from django.contrib.sites.shortcuts import get_current_site
from django.conf import settings

import urllib

# code 요청
def kakao_login(request):
    app_rest_api_key = str(settings.KAKAO_CID)
    print("=====================")
    redirect_uri = f"http://{settings.DOMAIN}/account/login/kakao/callback/"
    print(redirect_uri)
    print("=====================")
    redirect_url = f"https://kauth.kakao.com/oauth/authorize?client_id={app_rest_api_key}&redirect_uri={redirect_uri}&response_type=code"
    print(redirect_url)
    return redirect(redirect_url)

# access token 요청
def kakao_callback(request):
    params = urllib.parse.urlencode(request.GET)
    absurl = f"http://{settings.DOMAIN}/account/login/kakao/callback?{params}"
    print("absurl: "+absurl)
    return redirect(absurl)
