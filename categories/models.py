from django.db import models

# Create your models here.


class Category(models.Model):
    id = models.BigAutoField(primary_key=True, auto_created=True)
    name = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
