from rest_framework import serializers
from .models import Product
from django.core.exceptions import ValidationError

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'stock', 'created_at']

    def validate_price(self, value):
        """Validasi harga agar lebih dari 0"""
        if value <= 0:
            raise serializers.ValidationError("Price must be greater than 0.")
        return value

    def validate_stock(self, value):
        """Validasi stok agar tidak negatif"""
        if value < 0:
            raise serializers.ValidationError("Stock cannot be negative.")
        return value
