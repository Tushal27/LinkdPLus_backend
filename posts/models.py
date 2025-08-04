from django.db import models
from django.conf  import settings
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.
class Posts(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE , related_name='posts')
    title = models.CharField(max_length=100)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User,related_name="liked_posts",blank=True)
    dislikes = models.ManyToManyField(User, related_name="disliked_posts",blank=True)
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created']


class Comments(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.user} commented on {self.post.title}'
