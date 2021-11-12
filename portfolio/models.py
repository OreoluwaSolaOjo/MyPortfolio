from os import name
from django.db import models

# Create your models here.


class Contact(models.Model):
    txtName = models.TextField()
    txtEmail = models.TextField()
    txtPhone = models.TextField()
    txtMsg = models.TextField()

    def __str__(self):
        return self.txtName
