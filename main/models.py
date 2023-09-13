from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    date_added = models.DateField(auto_now_add=True)
    amount = models.IntegerField()
    description = models.TextField()
    category = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return self.name
