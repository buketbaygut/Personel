from django.db import models

# Create your models here.

class Personel(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    isPublished = models.BooleanField(default=True)

    def __str__(self):
        return self.name