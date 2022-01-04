from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.


class Game(models.Model):
    title = models.CharField(max_length=255,blank=True,null=True)
    publisher = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,null=True, blank=True)
    price = models.IntegerField(blank=True, null=True)
    description = models.TextField(default="")

    def __str__(self):
        return self.title
    