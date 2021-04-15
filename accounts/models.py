from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager

# Create your models here.
class User(AbstractUser):

    REGISTER_LOGIN_EMAIL = "email"
    REGISTER_LOGIN_KAKAO = "kakao"
    REGISTER_LOGIN_METHOD = (
        (REGISTER_LOGIN_EMAIL, "Email"),
        (REGISTER_LOGIN_KAKAO, "Kakao"),
    )

    USER_TYPE_ENTERPRISE = "enterprise"
    USER_TYPE_WORKER = "worker"
    USER_TYPE_METHOD = (
        (USER_TYPE_ENTERPRISE, "Enterprise"),
        (USER_TYPE_WORKER, "Worker"),
    )

    username = None
    email = models.EmailField(_('email address'), unique=True)
    register_user_method = models.CharField(
        max_length=50, choices=USER_TYPE_METHOD, default=USER_TYPE_WORKER
    )
    register_login_method = models.CharField(
        max_length=50, choices=REGISTER_LOGIN_METHOD, default=REGISTER_LOGIN_EMAIL
    )


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
