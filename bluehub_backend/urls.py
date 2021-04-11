from allauth.account.views import confirm_email
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from accounts.views import kakao_login, kakao_callback
urlpatterns = [
    path('admin/', admin.site.urls),
    url('rest-auth/', include('rest_auth.urls')),
    url('rest-auth/registration/', include('rest_auth.registration.urls')),
    url('account/', include('allauth.urls')),
    url('accounts-rest/registration/account-confirm-email/(?P<key>.+)/$', confirm_email,
        name='account_confirm_email'),
    path('', include('django.contrib.auth.urls')),
    path('account/login/kakao/', kakao_login, name='kakao_login'),
    path('account/login/kakao/callback/', kakao_callback, name='kakao_callback'),
]

