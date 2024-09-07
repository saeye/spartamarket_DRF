# accounts/serializers.py
from rest_framework import serializers
from .models import CustomUser
from .validators import validate_username, validate_nickname, validate_email_unique

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'name', 'nickname', 'email', 'birth', 'password', 'gender', 'introduction']

    def validate_username(self, value):
        validate_username(value)
        return value
    
    def validate_nickname(self, value):
        validate_nickname(value)
        return value

    def validate_email(self, value):
        validate_email_unique(value)
        return value

    def create(self, validated_data):
        user = CustomUser(**validated_data)
        user.set_password(validated_data['password'])  
        user.save()
        return user
