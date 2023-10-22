from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from PIL import Image as PILImage
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile



# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=200, verbose_name="username")
    photo_avatar = models.ImageField(upload_to="images/avatars/%Y/%m/%d")
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=40)
    def __str__(self):
        return f"{self.username}"

class Photo(models.Model):
    name = models.CharField(max_length=200)
    original = models.ImageField(upload_to='photos/%Y/', verbose_name="Original photo")
    thumbnail = models.ImageField(upload_to='thumbnails/', blank=True, null=True)
    def __str__(self):
        return f"{self.name}"
    
class Album(models.Model):
    name = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=1500)
    photoes = models.ManyToManyField(Photo)

    def __str__(self):
        return f"{self.name}"


@receiver(pre_save, sender=Photo)
def generate_thumbnail(sender, instance, **kwargs):
    if instance.original:
        image = PILImage.open(instance.original)
        image.thumbnail((384, 216))
        thumb_io = BytesIO()
        image.save(thumb_io, format='PNG')  
        instance.thumbnail.save(instance.original.name, InMemoryUploadedFile(
            thumb_io, None, f'thumbnail_{instance.original.name}', 'image/jpeg', thumb_io.tell(), None
        ), save=False)