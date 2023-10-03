from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=255)
    date_added = models.DateField(auto_now_add=True)
    amount = models.IntegerField(default=0)  # Ini mewakili jumlah stok
    description = models.TextField()
    category = models.TextField()
    price = models.IntegerField()  # Kembalikan ke bidang 'price' tanpa 'price_per_item'
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
