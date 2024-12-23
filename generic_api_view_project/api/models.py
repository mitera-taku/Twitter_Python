from django.db import models
from django.contrib.auth.models import User 

class Post(models.Model):
    title = models.CharField(max_length=255)  # type: ignore
    content = models.TextField() # type: ignore
    author = models.ForeignKey(User, on_delete=models.CASCADE) # type: ignore
    created_at = models.DateTimeField(auto_now_add=True) # type: ignore
    
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments') # type: ignore
    author = models.ForeignKey(User, on_delete=models.CASCADE) # type: ignore
    comment = models.TextField() # type: ignore
    created_at = models.DateTimeField(auto_now_add=True) # type: ignore
    

class MediaPost(models.Model):
    title = models.CharField(max_length=100)# type: ignore
    description = models.TextField(blank=True, null=True)# type: ignore
    image = models.ImageField(upload_to='images/', blank=True, null=True) # type: ignore
    video = models.FileField(upload_to='videos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)# type: ignore
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)# type: ignore  # デフォルトユーザー ID


    def __str__(self):
        return self.title
    
