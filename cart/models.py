from django.db import models
from django.contrib.auth.models import User
from item.models import Item

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ManyToManyField(Item, through='CartItem')

    def __str__(self):
        return f"{self.user.username}'s Cart"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.cart.user.username}'s cart: {self.item.name}"