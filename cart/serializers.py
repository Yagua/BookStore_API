from rest_framework import serializers
from core.models import ShoppingCart, ShoppingCartItem
from library.serializers import BookSerializer


class ShoppingCartItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = ShoppingCartItem
        fields = ("id", "book", "quantity")


class ShoppingCartItemObjectSerializer(serializers.ModelSerializer):

    book = BookSerializer(required=False)

    class Meta:
        model = ShoppingCartItem
        fields = ("id", "book", "quantity")


class ShoppingCartSerializer(serializers.ModelSerializer):

    items = ShoppingCartItemObjectSerializer(
        many=True, required=False, allow_empty=True
    )

    class Meta:
        model = ShoppingCart
        fields = (
            "id",
            "user",
            "items",
        )
