from django.contrib import admin
from .models import Profile,Post,like,News,Categories,NewsImage
# Register your models here.
# admin.site.register(Profile)
# admin.site.register(Post)
admin.site.register(like)
admin.site.register(News)
admin.site.register(Categories)
admin.site.register(NewsImage)