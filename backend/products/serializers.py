from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField() # Set it's value  in discount from models 

    class Meta:
        model = Product
        fields = [
            'title',
            'content',
            'price',
            'sale_price',
            'my_discount'
        ]

    def get_my_discount(self, obj): # Attach get up in the function for take the attribute and set in in another attribute
        try:
            return obj.get_discount()
        except:
            return None
