from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class OpsUser(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=10)
    password = models.CharField(max_length=10)
    def __str__(self):
        return self.username

class File(models.Model):
    user = models.ForeignKey(OpsUser, on_delete=models.CASCADE)
    file = models.FileField(upload_to='files')
    def __str__(self):
        return self.user.username