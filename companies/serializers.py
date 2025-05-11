from rest_framework import serializers
from .models import Company

class CompanyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name', 'inn']
        
class CompanyDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class CompanyCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']