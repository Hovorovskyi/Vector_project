from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Захід'
        verbose_name_plural = 'Заходи'
