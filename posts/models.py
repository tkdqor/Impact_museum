from django.db import models

# Create your models here.

class Post(models.Model):

    product_name = models.CharField(max_length=100)
    brand = models.TextField()
    created_at = models.DateTimeField()

    def __str__(self):
        return f'{self.product_name}: {self.brand}'