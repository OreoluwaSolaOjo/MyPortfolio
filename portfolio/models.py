from os import name
from django.db import models

# Create your models here.


class Contact(models.Model):
    txtName = models.CharField(max_length=200)
    txtEmail = models.EmailField(max_length=200, blank=True)
    txtPhone = models.CharField(max_length=200)
    txtMsg = models.TextField()

    def __str__(self):
        return self.txtName
