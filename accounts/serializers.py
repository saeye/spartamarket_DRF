from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

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
