from django.urls import path, include
from . import views

books_urls = [
    path("", views.BookList.as_view(), name="book_list"),
    path("<int:pk>/", views.BookDetail.as_view(), name="book_detail"),
    path("<int:pk>/categories/", views.book_categories, name="book_categories"),
]

categories_urls = [
]

authors_urls = [
]

urlpatterns = [
    path("books/", include(books_urls)),
    path("categories/", include(categories_urls)),
]
