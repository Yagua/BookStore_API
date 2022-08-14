from rest_framework import serializers
from core.models import Book, Category, Author


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
            "time_stamp",
        )
        extra_kwargs = {
            "maternal_last_name": {"required": False},
            "second_name": {"required": False},
            "books": {"required": False},
        }


class BookSerializer(serializers.ModelSerializer):
    """
    BookSerializer class for Book model
    """

    categories = CategorySerializer(many=True, required=False)
    authors = AuthorSerializer(many=True, required=False)

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

    def create(self, validated_data: dict):
        authors = validated_data.pop("authors")
        categories = validated_data.pop("categories")
        book = Book.objects.create(**validated_data)

        for author in authors:
            new_author = Author.objects.create(**author)
            new_author.books.add(book)

        for category in categories:
            new_category = Category.objects.create(**category)
            new_category.books.add(book)

        return book
