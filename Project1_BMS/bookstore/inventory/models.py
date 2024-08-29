from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    stock = models.IntegerField()
 
    def __str__(self):
        return self.title