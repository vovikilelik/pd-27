from django.db import models

# Create your models here.
from locations.models import Location


class User(models.Model):
    id = models.BigAutoField(primary_key=True, auto_created=True)
    first_name = models.TextField()
    last_name = models.TextField()
    username = models.TextField(max_length=50)
    password = models.TextField(max_length=50)
    role = models.CharField(max_length=20)
    age = models.IntegerField()

    locations = models.ManyToManyField(Location)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['username']
