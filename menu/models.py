from django.db import models


class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    category = models.CharField(max_length=255)
    image = models.ImageField(upload_to='menu_images/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Страва'
        verbose_name_plural = 'Страви'
