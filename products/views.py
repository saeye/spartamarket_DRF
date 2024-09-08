from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Product
from .serializers import ProductSerializer
from .pagination import CustomPagination
from rest_framework.exceptions import PermissionDenied
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


class ProductCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            product = serializer.save(user=request.user)
            return Response(ProductSerializer(product).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = CustomPagination  


class ProductUpdateView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        product = super().get_object()
        if product.user != self.request.user:
            raise PermissionDenied("수정 권한이 없습니다.")
        return product


class ProductDeleteView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, pk):
        try:
            product = Product.objects.get(id=pk)
        except Product.DoesNotExist:
            return Response({"error": "상품이 존재하지 않습니다."}, status=status.HTTP_404_NOT_FOUND)

        if request.user != product.user:
            return Response({"error": "삭제 권한이 없습니다."}, status=status.HTTP_403_FORBIDDEN)

        product.delete()
        return Response({"message": "상품이 삭제되었습니다."}, status=status.HTTP_204_NO_CONTENT)
    

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def product_like(request, pk):
    try:
        product = Product.objects.get(id=pk)
    except Product.DoesNotExist:
        return Response({"error": "상품이 존재하지 않습니다."}, status=status.HTTP_404_NOT_FOUND)

    user = request.user

    if product.likes.filter(id=user.id).exists():
        product.likes.remove(user)
        return Response({"좋아요 취소"}, status=status.HTTP_200_OK)
    else:
        product.likes.add(user)
        return Response({"좋아요"}, status=status.HTTP_200_OK)