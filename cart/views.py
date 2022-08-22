from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from django.shortcuts import get_object_or_404

from core.models import ShoppingCart, ShoppingCartItem, Book
from .serializers import ShoppingCartSerializer

@api_view(["GET"])
@permission_classes([IsAdminUser, IsAuthenticated])
def list_shopping_carts(request):
    """
    Get all shoppingcarts in dabatabe
    """

    queryset = ShoppingCart.objects.all()
    serializer = ShoppingCartSerializer(queryset, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["GET"])
def get_shopping_cart(request, pk):
    """
    Get an specific shoppingcart
    """

    cart = get_object_or_404(ShoppingCart, pk=pk)
    serializer = ShoppingCartSerializer(cart)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["POST"])
def add_item_to_cart(request, book_id):
    """
    Add a book in the user cart
    """

    book = get_object_or_404(Book, pk=book_id)
    cart = get_object_or_404(ShoppingCart, user=request.user)
    item, _ = ShoppingCartItem.objects.get_or_create(book=book)
    cart.items.add(item)
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(["DELETE"])
def remove_item_from_cart(request, item_id):
    """
    Remove specified item from user cart
    """

    item = get_object_or_404(ShoppingCartItem, pk=item_id)
    item.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
