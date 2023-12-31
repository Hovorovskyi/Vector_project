from django.db import models


class User(models.Model):
    username = models.CharField(unique=True, max_length=255)
    password = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(unique=True, max_length=20)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Користувач'
        verbose_name_plural = 'Користувачі'
