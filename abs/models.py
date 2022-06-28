from django.db import models


class Ad(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    name = models.TextField()
    author = models.TextField()
    price = models.FloatField()
    description = models.TextField()
    address = models.TextField()
    is_published = models.BooleanField()

    def __str__(self):
        return self.name


class Category(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    name = models.TextField()

    def __str__(self):
        return self.name
