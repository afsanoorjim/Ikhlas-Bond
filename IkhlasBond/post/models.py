from django.db import models

# Create your models here.

class Post(models.Model):
    post_description = models.TextField()
    post_image = models.ImageField(default=None)
    post_like = models.IntegerField(default=0)
    post_comments = models.TextField()

    def __str__(self):
        return self.post_description