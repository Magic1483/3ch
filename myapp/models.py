from django.db import models
from django.dispatch import receiver
from django.templatetags.static import static
import os

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=250)
    content = models.CharField(max_length=500,blank=True)
    img = models.ImageField( upload_to='media',blank=True)
    audio = models.FileField(blank=True,null=True)
    collection = models.CharField(max_length=100,default='non')
    author = models.CharField(null=True,max_length=50)

class User(models.Model):
  login = models.CharField(max_length=50)
  password = models.CharField(max_length=50)
  nick = models.CharField(max_length=50,null=True)

# Create your models here.
class Song(models.Model):
    title= models.TextField()
    image= models.ImageField(null=True,default=static('imgs/no_track_img.png'))
    audio_file = models.FileField(blank=True,null=True)
    paginate_by = 2

    def __str__(self):
        return self.title

@receiver(models.signals.post_delete, sender=Song)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `MediaFile` object is deleted.
    """
    if instance.audio_file:
        if os.path.isfile(instance.audio_file.path):
            os.remove(instance.audio_file.path)
          
class Video(models.Model):
  title = models.TextField()
  video = models.FileField(blank=True,null=True)