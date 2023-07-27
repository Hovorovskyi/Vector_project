from django.db import models
from user.models import User
from menu.models import MenuItem


class DeliveryOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(MenuItem)
    total_price = models.IntegerField()
    delivery_address = models.CharField(max_length=255)
