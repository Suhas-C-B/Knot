from rest_framework import serializers
from .models import User, Company, Supplier

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'companyName']

    def validate_companyName(self, value):
        if Company.objects.filter(companyName=value).exists():
            raise serializers.ValidationError("A Company with this name already exists.")
        return value
    
class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ['id', 'supplierName', 'company']

    def validate_supplierName(self, value):
        if Supplier.objects.filter(supplierName=value).exists():
            raise serializers.ValidationError("A supplier with this name already exists.")
        return value
    
class UserSerializer(serializers.ModelSerializer):

    company = CompanySerializer

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'company', 'supplier']

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("A user with this username already exists.")
        return value