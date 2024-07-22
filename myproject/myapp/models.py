# myapp/models.py

from django.db import models

class Company(models.Model):
    companyName = models.CharField(max_length=80, unique=True)

    def __str__(self):
        return self.companyName
    
class Supplier(models.Model):
    supplierName = models.CharField(max_length=80, unique=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='suppliers', null=True, blank=True)

    def __str__(self):
        return self.supplierName

class User(models.Model):
    username = models.CharField(max_length=80, unique=True)
    password = models.CharField(max_length=120)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='users', null=True, blank=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='users', null=True, blank=True)

    def __str__(self):
        return self.username
