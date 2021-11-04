from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    post_title = models.CharField(max_length=20)
    post_cat = models.CharField(max_length=20)
    post_publish_date = models.DateField()