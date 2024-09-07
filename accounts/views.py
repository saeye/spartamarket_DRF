from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from .serializers import UserSerializer
from .models import CustomUser
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import InvalidToken
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import permissions
from django.shortcuts import get_object_or_404

class SignupView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SigninView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        # 유저 인증
        user = authenticate(username=username, password=password)

        if user is None:
            return Response({"error": "존재하지 않는 유저네임이거나 틀린 비밀번호입니다"}, status=status.HTTP_400_BAD_REQUEST)

        # JWT 토큰 생성
        refresh = RefreshToken.for_user(user)

        res_data = {
            "access_token": str(refresh.access_token),
            "refresh_token": str(refresh),
        }

        return Response(res_data, status=status.HTTP_200_OK)


class SignoutView(APIView):
    def post(self, request):
        refresh_token = request.data.get("refresh_token")

        if not refresh_token:
            return Response({"error": "토큰이 제공되지 않았습니다."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
        except InvalidToken:
            return Response({"error": "유효하지 않은 토큰입니다."}, status=status.HTTP_400_BAD_REQUEST)

        return Response({"message": "로그아웃되었습니다."}, status=status.HTTP_205_RESET_CONTENT)
    

class ProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated] 

    def get(self, request, username):
        if request.user.is_authenticated:
            user = get_object_or_404(CustomUser, username=username)
            serializer = UserSerializer(user)
            return Response(serializer.data, status=200)
        else:
            return Response({"error": "로그인 후 조회할 수 있습니다."}, status=status.HTTP_401_UNAUTHORIZED)
