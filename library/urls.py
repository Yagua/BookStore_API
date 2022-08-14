from django.urls import path, include
from . import views

app_name = "library"

books_urls = [
    path("", views.BookList.as_view(), name="book_list"),
    path("<int:pk>/", views.BookDetail.as_view(), name="book_detail"),
    path("<int:pk>/categories/", views.book_categories, name="book_categories"),
]

categories_urls = [
    path("", views.CategoryList.as_view(), name="category_list"),
    path("<int:pk>/", views.CategoryDetail.as_view(), name="category_detail"),
    path("<int:pk>/books/", views.category_books, name="category_books"),
]

authors_urls = [
    path("", views.AuthorList.as_view(), name="author_list"),
    path("<int:pk>/", views.AuthorDetail.as_view(), name="author_detail"),
    path("<int:pk>/books/", views.author_books, name="author_books"),
]

urlpatterns = [
    path("books/", include(books_urls)),
    path("categories/", include(categories_urls)),
    path("authors/", include(authors_urls)),
]
