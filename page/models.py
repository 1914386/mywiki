from django.db import models
from django.utils import timezone
from django.conf import settings

# Create your models here.

# 게시글 모델
class Post(models.Model):
    title = models.CharField(max_length=50, default='')
    update_date = models.DateTimeField(default=timezone.now)
    text = models.TextField()
    image = models.ImageField(upload_to="images/", blank=True, null=True)

    def __str__(self):
        return self.title

# 댓글 모델
class Comment(models.Model):
    content = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)