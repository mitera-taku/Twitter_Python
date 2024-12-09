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
