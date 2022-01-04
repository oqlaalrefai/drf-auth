from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class GamePublisher(AbstractUser):
    favorite_thing = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)

    REQUIRED_FIELDS = ['favorite_thing', 'country']

    class Meta:
        verbose_name = "GamePublisher"
        verbose_name_plural = "GamePublishers"
    
    def __str__(self):
        return self.username
