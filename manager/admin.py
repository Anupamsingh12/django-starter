from django.contrib import admin
from .models import Profile,Post,like,BlogPost
# Register your models here.
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(like)
admin.site.register(BlogPost)