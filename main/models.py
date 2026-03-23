from django.db import models
from cloudinary_storage.storage import MediaCloudinaryStorage

media_storage = MediaCloudinaryStorage()

# Create your models here.
class Note(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
class Memory(models.Model):
    name = models.CharField(max_length=100)
    # Bind storage explicitly so Django doesn't try to write to the local
    # filesystem (which can be read-only on serverless platforms).
    photo = models.ImageField(upload_to='memories/', storage=media_storage)
    caption = models.CharField(max_length=255, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)