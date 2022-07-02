from django.db import models

# Create your models here.


class Location(models.Model):
    id = models.BigAutoField(primary_key=True, auto_created=True)
    name = models.TextField()
    lat = models.CharField(max_length=20)
    lon = models.TextField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'
