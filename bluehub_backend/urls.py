from allauth.account.views import confirm_email
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from accounts.views import kakao_login, kakao_callback, KakaoToDjangoLogin
urlpatterns = [
    path('admin/', admin.site.urls),

    # 로그인
    path('account/', include('rest_auth.urls')),
    path('account/registration/', include('rest_auth.registration.urls')),
    path('account/', include('allauth.urls')),
    url(r'account/registration/confirm-email/(?P<key>.+)/$', confirm_email, name='confirm_email'),
    path('', include('django.contrib.auth.urls')),

    # path('admin/', admin.site.urls),
    # url('rest-auth/', include('rest_auth.urls')),
    # url('rest-auth/registration/', include('rest_auth.registration.urls')),
    # url('account/', include('allauth.urls')),
    # url('accounts-rest/registration/account-confirm-email/(?P<key>.+)/$', confirm_email,
    #     name='account_confirm_email'),
    # path('', include('django.contrib.auth.urls')),

    # 소셜 로그인
    path('account/login/kakao/', kakao_login, name='kakao_login'),
    path('account/login/kakao/callback/', kakao_callback, name='kakao_callback'),
    path('account/login/kakao/todjango', KakaoToDjangoLogin.as_view(), name='kakao_todjango_login'),
]

