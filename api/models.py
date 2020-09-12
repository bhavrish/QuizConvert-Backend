from django.db import models

# Create your models here.
class Video(models.Model):
    name = models.CharField(max_length=60)
    category = models.CharField(max_length=60)
    
    def __str__(self):
        return self.name