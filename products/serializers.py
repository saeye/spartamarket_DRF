from rest_framework import serializers
from .models import Product
from .validators import validate_required_field

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['title', 'content', 'image']

    def validate(self, data):
        data['title'] = validate_required_field(data.get('title'), "상품명")
        
        data['content'] = validate_required_field(data.get('content'), "내용")
        
        return data
