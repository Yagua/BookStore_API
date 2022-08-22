from rest_framework import serializers
from core.models import ShoppingCart, ShoppingCartItem


class ShoppingCartItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = ShoppingCartItem
        fields = ("id", "book", "quantity", "time_stamp")


class ShoppingCartSerializer(serializers.ModelSerializer):

    items = ShoppingCartItemSerializer(
        many=True, required=False, allow_empty=True
    )

    class Meta:
        model = ShoppingCart
        fields = (
            "id",
            "user",
            "items",
            "time_stamp",
        )
