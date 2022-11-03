from django.db import models

class Shop(models.Model):
    title = models.CharField(max_length=100, unique=True)
    photo = models.ImageField(upload_to='shop_photo')
    description = models.CharField(max_length=500, blank=True)
    price = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.title}'