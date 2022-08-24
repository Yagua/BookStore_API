from django.urls import path
from . import views

app_name = "cart"

urlpatterns = [
    path("", views.list_shopping_carts, name="cart_list"),
    path("user-cart/", views.get_shopping_cart, name="cart_retrive"),
    path("add-item/", views.add_item_to_cart, name="add_item_to_cart"),
    path("remove-item/<int:item_id>/",
        views.remove_item_from_cart, name="remove_item_from_cart"
    ),
    path('items/', views.get_user_cart_items, name="user_cart_items"),
    path("update-item/", views.update_cart_item, name="update_cart_item")
]
