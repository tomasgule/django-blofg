from django.db import models
from django.conf import settings

# Create your models here.
class Blogpost(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="blogpost", on_delete=models.CASCADE
    )
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=1000)
    created_at = models.DateField(auto_now=True)
    post_image = models.ImageField()
