from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    phone=models.CharField(max_length=15,blank=True)
    dp=models.ImageField(upload_to="profile_pic")
    def __str__(self):
        return "{}".format(self.user)

class Post(models.Model):
    
    profile=models.ForeignKey(Profile,on_delete=models.CASCADE,null=True,blank=True)
    img=models.ImageField(upload_to="post_image",blank=True)
    written_text=models.TextField(max_length=1000,blank=True)
    time=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return "{}'s post".format(self.profile.user)

class like(models.Model):
    post=models.ForeignKey(Post,null=True,on_delete=models.CASCADE)
    profile=models.ForeignKey(Profile,on_delete=models.DO_NOTHING)
    time=models.DateTimeField(auto_now=True)
    dislike=models.IntegerField(default=0)