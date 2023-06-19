from django.db import models

class UserProfile(models.Model):
    name = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=250, null=True)
    phone = models.CharField(max_length=10, null=True)
    password = models.CharField(max_length=100, null=True)
    date_created = models.DateTimeField(auto_now_add=True)