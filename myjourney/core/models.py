from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=300, null=True)
    email = models.EmailField(max_length=100, null=True)
