# accounts/validators.py
from django.core.validators import validate_email
from django.core.exceptions import ValidationError as DjangoValidationError
from .models import CustomUser


def validate_username(username):
    if CustomUser.objects.filter(username=username).exists():
        raise DjangoValidationError("이미 사용 중인 username입니다.")

def validate_nickname(nickname):
    if len(nickname) > 20:
        raise DjangoValidationError("너무 길어요. 20자 이하로 입력해주세요.")
    if CustomUser.objects.filter(nickname=nickname).exists():
        raise DjangoValidationError("이미 사용 중인 nickname입니다.")

def validate_email_unique(email):
    try:
        validate_email(email)
    except DjangoValidationError:
        raise DjangoValidationError("이메일 형식이 아닙니다.")
    if CustomUser.objects.filter(email=email).exists():
        raise DjangoValidationError("이미 사용 중인 email입니다.")

