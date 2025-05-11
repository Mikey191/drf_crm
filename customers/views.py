from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from .models import Customer, Status, Tag
from .serializers import (
    CustomerCreateUpdateSerializer, 
    CustomerDetailSerializer, 
    CustomerListSerializer, 
    StatusSerializer, 
    TagSerializer
)

class 