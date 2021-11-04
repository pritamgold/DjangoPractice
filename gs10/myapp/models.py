from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.db.models.deletion import CASCADE, PROTECT

# Create your models here.

class Page(models.Model):
    user = models.OneToOneField(User, on_delete=CASCADE,primary_key=True)
    #user = models.OneToOneField(User, on_delete=PROTECT,primary_key=True)
    #user = models.OneToOneField(User, on_delete=CASCADE,primary_key=True,
    #limit_choices_to={'is_staff':True})
    page_name = models.CharField(max_length=25)
    page_cat = models.CharField(max_length=20)
    page_publish_date = models.DateField()

class Like(Page):
    panna = models.OneToOneField(Page, on_delete=CASCADE, parent_link=True, primary_key=True)
    likes = models.IntegerField()

