from django.db import models
from django.conf import settings


class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField(default="")

    def __str__(self):
        return f"{self.title} {self.price} руб."


class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)  
    quantity = models.IntegerField(default=1)  
    ordered = models.BooleanField(default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.item.title} amount={self.quantity}"


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username





