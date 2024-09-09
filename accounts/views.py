from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status, permissions
from django.shortcuts import get_object_or_404
from .serializers import UserSerializer, UserProfileSerializer
from .models import CustomUser

# 회원가입
class SignupView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 로그인
class SigninView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username, password=password)

        if not user:
            return Response({"error": "유저네임 또는 비밀번호가 올바르지 않습니다"}, status=status.HTTP_400_BAD_REQUEST)
        
        # 인증 후 토큰 발급
        refresh = RefreshToken.for_user(user)
        return Response({
            "access_token": str(refresh.access_token),
            "refresh_token": str(refresh)
        }, status=status.HTTP_200_OK)

# 로그아웃
class SignoutView(APIView):
    def delete(self, request):
        refresh_token = request.data.get("refresh_token")

        if not refresh_token:
            return Response({"error": "토큰이 제공되지 않았습니다."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            RefreshToken(refresh_token).blacklist()
            return Response({"message": "로그아웃되었습니다."}, status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response({"error": "유효하지 않은 토큰입니다."}, status=status.HTTP_400_BAD_REQUEST)


# 프로필 조회
class ProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated] 

    def get(self, request, username):
        user = get_object_or_404(CustomUser, username=username)
        serializer = UserProfileSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
