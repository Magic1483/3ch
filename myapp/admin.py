from django.contrib import admin
from .models import Post,User,Song,Video
# Register your models here.

admin.site.register(Post)
admin.site.register(User)
admin.site.register(Song)
admin.site.register(Video)