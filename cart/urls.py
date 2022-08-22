from django.urls import path
from . import views

app_name = "cart"

urlpatterns = [
    path("", views.list_shopping_carts, name="cart_list"),
    path("<int:pk>/", views.get_shopping_cart, name="cart_retrive"),
    path("add-item/<int:book_id>/",
        views.add_item_to_cart, name="add_item_to_cart"
    ),
    path("remove-item/<int:item_id>/",
        views.remove_item_from_cart, name="remove_item_from_cart"
    )
]
