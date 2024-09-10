from rest_framework import serializers
from .models import CustomUser
from .validators import validate_username, validate_nickname, validate_email_unique

class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(validators=[validate_username])
    nickname = serializers.CharField(validators=[validate_nickname])
    email = serializers.EmailField(validators=[validate_email_unique])

    class Meta:
        model = CustomUser
        fields = ['username', 'name', 'nickname', 'email', 'birth', 'password', 'gender', 'introduction']

    def create(self, validated_data):
        user = CustomUser(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'nickname', 'email', 'birth', 'introduction']
