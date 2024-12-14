from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class Speaker(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    bio = models.TextField()
    photo = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return self.name