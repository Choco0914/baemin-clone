from django.db import models
from django.contrib.auth.models import User

class Partner(models.Model):
    """업체에 대한 정보"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    description = models.TextField()
