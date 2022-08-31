from django.urls import path

from . import views

urlpatterns = [
    path("books/", views.SearchBook.as_view(), name="search_book")
]
