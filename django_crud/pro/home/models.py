from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    image = models.ImageField(default='default.png', upload_to='post_pictures')
    para = models.TextField(max_length=500)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='profilepic.jpg', upload_to='profile_pictures')
    dob = models.DateField(blank=False)

    def __str__(self):
        return self.user.username