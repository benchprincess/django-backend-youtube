from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin


# - email
# - password => 설정 따로 필요 없음
# - nickname
# - is_business(boolean): personal, business

class User(AbstractUser, PermissionsMixin):
    email = models.CharField(max_length=30, unique=True)
    nickname = models.CharField(max_length=255)

    is_business = models.BooleanField(default=False)
    is_active = models.BooleanField(defalut=True)
    is_staff = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'

    def __str__(self):
        return f"email:{self.email}, nickname: {self.nickname}"