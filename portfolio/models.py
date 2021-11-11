from os import name
from django.db import models

# Create your models here.


class Contact(models.Model):
    txtName = models.TextField()
    txtEmail = models.EmailField(max_length=70, blank=True)
    txtPhone = models.CharField(max_length=15)
    txtMsg = models.TextField()

    def __str__(self):
        return self.txtName
