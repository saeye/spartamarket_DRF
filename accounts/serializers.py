from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    
    # 비밀번호 쓰기전용 처리
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'name', 'nickname', 'email', 'birth', 'password', 'gender', 'introduction']


    # 회원가입한 유저 인스턴스 생성 후 pw 해싱하여 DB 저장
    def create(self, validated_data):
        user = CustomUser(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


# 유저 프로필 조회 시
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'nickname', 'email', 'birth', 'introduction']
