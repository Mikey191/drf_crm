from rest_framework import generics
from .models import Company
from .serializers import CompanySerializer
from .permissions import CompanyPermission


class CompanyListCreateView(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [CompanyPermission]
    
class CompanyRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanyPermission
    permission_classes = [CompanyPermission]