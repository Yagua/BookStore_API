from django.contrib import admin
from . import models

admin.site.register([
    models.User,
    models.UserProfile,
    models.Book,
    models.Category,
    models.ShoppingCart,
    models.ShoppingCartItem,
    models.Author,
])
