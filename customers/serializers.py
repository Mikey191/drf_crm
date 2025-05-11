from rest_framework import serializers
from .models import Customer, Status, Tag
from users.serializers import UserListSerializer
from companies.serializers import CompanyListSerializer

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ['id', 'name', 'color']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name', 'color']
        
      
# Базовый сериализатор  
class CustomerDetailSerializer(serializers.ModelSerializer):
    manager = UserListSerializer(read_only=True)
    company = CompanyListSerializer(read_only=True)
    status = StatusSerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Customer
        fields = '__all__'

class CustomerListSerializer(serializers.ModelSerializer):
    status = StatusSerializer(read_only=True)
    company = CompanyListSerializer(read_only=True)

    class Meta:
        model = Customer
        fields = ['id', 'first_name', 'last_name', 'email', 'phone', 'status', 'company']
        

class CustomerCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = [
            'last_name', 'first_name', 'middle_name', 'email', 'phone', 'manager', 'company', 'status', 'tags'
        ]