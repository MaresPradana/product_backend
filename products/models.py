from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100, validators=[MinLengthValidator(3)])
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'products'

    def __str__(self):
        return self.name