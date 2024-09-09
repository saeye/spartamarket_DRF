from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from .models import CustomUser

def validate_username(value):
    if CustomUser.objects.filter(username=value).exists():
        raise ValidationError("이미 사용 중인 유저 이름입니다.")
    return value

def validate_nickname(value):
    if CustomUser.objects.filter(nickname=value).exists():
        raise ValidationError("이미 사용 중인 닉네임입니다.")
    return value

def validate_email_unique(value):
    if CustomUser.objects.filter(email=value).exists():
        raise ValidationError("이미 사용 중인 이메일입니다.")
    return value
