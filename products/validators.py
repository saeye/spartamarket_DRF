from rest_framework import serializers

def validate_required_field(value, field_name):
    #title or content가 비어있을 경우
    if not value:
        raise serializers.ValidationError(f"{field_name}을(를) 입력해주세요.")
    return value

