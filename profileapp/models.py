from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(default='John Doe (Default)', max_length=200, null=True)
    title = models.CharField(default='This is tha default , title change it in profile. ',max_length=200, null=True)
    desc_text = 'Hey there is a default text descripton about you that you can change on after clicking on "Edit" or going'
    profile_img = models.ImageField(default='media/default.jpg', upload_to='media', null=True, blank=True)
    def __str__(self):
        return f"{self.user.usernmae}'s profile"

        