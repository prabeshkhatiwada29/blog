from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    author = models.CharField(max_length=100)
    tags = models.CharField(max_length=100, blank=True, null=True)
    comments_count = models.PositiveIntegerField(default=0)
    likes_count = models.PositiveIntegerField(default=0)
    is_published = models.BooleanField(default=True)
    

    def __str__(self):
        return self.title
