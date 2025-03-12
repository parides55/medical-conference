from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class PresidentMessage(models.Model):
    
    STATUS = (
        (1, 'president'),
        (2, 'not president'),
    )
    
    title = models.CharField(max_length=100)
    message = models.TextField()
    image = CloudinaryField('image', default='placeholder')
    status = models.IntegerField(choices=STATUS, default=1)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.title