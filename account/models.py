from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class Account(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  username = models.CharField(null=True, max_length=30)
  profile_pic = CloudinaryField('image', default="/home/cseiei/Code/python/Digi-Backend/theboi.gif")
  def __str__(self):
    return self.username



class Post(models.Model):
  account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='posts')
  content = models.TextField(null=True)
  caption = CloudinaryField('image')
  def __str__(self):
    return self.content



class Comment(models.Model):
  content = models.TextField()
  post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
  account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='comments')
  def __str__(self):
    return self.content


