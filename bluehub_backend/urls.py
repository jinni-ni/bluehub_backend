from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from allauth.account.views import confirm_email
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

from accounts.views import kakao_login, kakao_callback, KaKaoSocialLoginView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include("accounts.urls")),
    # 로그인
    # path('account/', include('rest_auth.urls')),
    # path('account/registration/', include('rest_auth.registration.urls')),
    # path('account/', include('allauth.urls')),
    # url(r'account/registration/confirm-email/(?P<key>.+)/$', confirm_email, name='confirm_email'),
    # path('', include('django.contrib.auth.urls')),
    # # 소셜 로그인
    # path('account/login/kakao/', kakao_login, name='kakao_login'),
    # path('account/login/kakao/callback/', kakao_callback, name='kakao_callback'),
    # path('account/login/kakao/todjango', KaKaoSocialLoginView.as_view(), name='kakao_todjango_login'),
    #
    # path('token/', obtain_jwt_token),
    # path('token/refresh/', refresh_jwt_token),
    # path('token/verify', verify_jwt_token),

    path('', include("recruit.urls")),
]

