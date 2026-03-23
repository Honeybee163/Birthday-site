from django.db import models

# Create your models here.
class Note(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
class Memory(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='memories/')
    caption = models.CharField(max_length=255, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)