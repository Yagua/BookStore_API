from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from core.models import ShoppingCart, ShoppingCartItem, Book
from .serializers import ShoppingCartSerializer, ShoppingCartItemSerializer
from utils.model_tools import get_instance

@api_view(["GET"])
@permission_classes([IsAdminUser, IsAuthenticated])
def list_shopping_carts(request):
    """
    Get all shoppingcarts in dabatabe
    """

    queryset = ShoppingCart.objects.all()
    serializer = ShoppingCartSerializer(queryset, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["POST"])
def add_item_to_cart(request):
    """
    Add a book in the user cart
    """

    try:
        book_id = int(request.data.get("book_id", ''))
        quantity = request.data.get("quantity", '')
    except ValueError:
        return Response({
            "error": "The 'book_id' and 'quantity' must be intengers values."
        }, status=status.HTTP_400_BAD_REQUEST)

    exist, result = get_instance(Book, pk=book_id)
    if not exist:
        return result

    cart = ShoppingCart.objects.get(user=request.user)

    if cart.items.filter(book=result).exists():
        existent_item = cart.items.get(book=result)
        existent_item.quantity = quantity
        existent_item.save()
    else:
        item = ShoppingCartItem.objects.create(book=result, quantity=quantity)
        cart.items.add(item)

    serializer = ShoppingCartSerializer(cart)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["DELETE"])
def remove_item_from_cart(request, item_id):
    """
    Remove specified item from user cart
    """

    cart = ShoppingCart.objects.get(user=request.user)
    if not cart.items.filter(pk=item_id).exists():
        return Response({
            "error": "The item '{0}' is not in the cart.".format(item_id)
        }, status=status.HTTP_404_NOT_FOUND)

    item = cart.items.get(pk=item_id)
    item.delete()
    serializer = ShoppingCartSerializer(cart)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def get_shopping_cart(request):
    """
    Get an specific shoppingcart
    """

    cart = ShoppingCart.objects.get(user=request.user)
    serializer = ShoppingCartSerializer(cart)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def get_user_cart_items(request):
    """
    Get all user shoppingcart items in database
    """

    cart = ShoppingCart.objects.get(user=request.user)
    serializer = ShoppingCartItemSerializer(cart.items, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["PUT"])
def update_cart_item(request):
    """
    Update a shoppingcart item
    """

    try:
        book_id = int(request.data.get("book_id", ''))
        quantity = int(request.data.get("quantity", ''))
    except ValueError:
        return Response({
            "error": "The 'book_id' and 'quantity' must be intengers values."
        }, status=status.HTTP_400_BAD_REQUEST)

    exists, result = get_instance(Book, pk=book_id)
    if not exists:
        return result

    cart = ShoppingCart.objects.get(user=request.user)

    item = cart.items.filter(book=result)
    if not item.exists():
        return Response({
            "error": "This book is not in the cart."
        }, status=status.HTTP_400_BAD_REQUEST)

    item.update(quantity=quantity)
    serializer = ShoppingCartSerializer(cart)
    return Response(serializer.data, status=status.HTTP_200_OK)
