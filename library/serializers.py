from rest_framework import serializers
from core.models import Book, Category, Author

class BookSerializer(serializers.ModelSerializer):
    """
    BookSerializer class for Book model
    """

    class Meta:
        model = Book
        fields = (
            "id",
            "title",
            "description",
            "cover",
            "edition",
            "language",
            "page_number",
            "publishier",
            "rating",
            "available",
            "categories",
            "authors",
            "time_stamp",
        )


class CategorySerializer(serializers.ModelSerializer):
    """
    CategorySerializer class for Category model
    """

    class Meta:
        model = Category
        fields = ("id", "name", "time_stamp")


class AuthorSerializer(serializers.ModelSerializer):
    """
    AuthorSerializer class for Author model
    """

    class Meta:
        model = Author
        fields = (
            "first_name",
            "second_name",
            "paternal_last_name",
            "maternal_last_name",
            "picture",
            "country",
            "books",
            "time_stamp"
        )
