from django.test import TestCase
from core.models import Author, Book, Category
from library.serializers import (
    AuthorSerializer,
    BookSerializer,
    CategorySerializer,
)

BOOK_ATTRS = {
    "title": "The Go Programming Language",
    "description": "The Go Programming Language is the authoritative\
resource for any programmer who wants to learn Go",
    "cover": None,
    "edition": "1st",
    "language": "English",
    "page_number": 368,
    "publishier": "Addison-Wesley Professional",
    "rating": 5.7,
    "available": True,
}

CATEGORY_ATTRS = {"name": "Action"}

AUTHOR_ATTRS = {
    "first_name": "Gabriel",
    "second_name": "Jose",
    "paternal_last_name": "Garcia",
    "maternal_last_name": "Marquez",
    "country": "Colombia",
}


class BookSerializerTestCase(TestCase):

    def test_serialize_book_successfully(self):
        """
        Serializer a book sucessfully
        """

        book = Book.objects.create(**BOOK_ATTRS)
        serializer = BookSerializer(book)

        self.assertEqual(book.title, serializer.data["title"])
        self.assertEqual(book.description, serializer.data["description"])
        self.assertEqual(book.cover, serializer.data["cover"])
        self.assertEqual(book.edition, serializer.data["edition"])
        self.assertEqual(book.language, serializer.data["language"])
        self.assertEqual(book.page_number, serializer.data["page_number"])
        self.assertEqual(book.publishier, serializer.data["publishier"])
        self.assertEqual(book.rating, serializer.data["rating"])
        self.assertEqual(book.available, serializer.data["available"])

    def test_deserialize_book_successfully(self):
        """
        Deserialize a book sucessfully
        """

        serializer = BookSerializer(data=BOOK_ATTRS)

        self.assertTrue(serializer.is_valid())
        self.assertEqual(
                serializer.validated_data["title"], BOOK_ATTRS["title"])
        self.assertEqual(
                serializer.validated_data["description"], BOOK_ATTRS["description"])
        self.assertEqual(
                serializer.validated_data["cover"], BOOK_ATTRS["cover"])
        self.assertEqual(
                serializer.validated_data["edition"], BOOK_ATTRS["edition"])
        self.assertEqual(
                serializer.validated_data["language"], BOOK_ATTRS["language"])
        self.assertEqual(
                serializer.validated_data["page_number"], BOOK_ATTRS["page_number"])
        self.assertEqual(
                serializer.validated_data["publishier"], BOOK_ATTRS["publishier"])
        self.assertEqual(
                serializer.validated_data["rating"], BOOK_ATTRS["rating"])
        self.assertEqual(
                serializer.validated_data["available"], BOOK_ATTRS["available"])
        self.assertFalse(bool(serializer.errors))

    def test_deserialize_book_unsuccessfully(self):
        """
        Deserialize a book unsucessfully
        (empty payload)
        """

        serializer = BookSerializer(data={})
        self.assertFalse(serializer.is_valid())
        self.assertTrue(bool(serializer.errors))


class CategorySerializerTestCase(TestCase):

    def test_serialize_category_sucessfully(self):
        """
        Serialize sucessfully a category
        """

        category = Category(**CATEGORY_ATTRS)
        serializer = CategorySerializer(category)

        self.assertEqual(category.name, serializer.data["name"])

    def test_deserialize_category_successfully(self):
        """
        Deserialize a category sucessfully
        """

        serializer = CategorySerializer(data=CATEGORY_ATTRS)

        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.data["name"], CATEGORY_ATTRS["name"])
        self.assertFalse(bool(serializer.errors))

    def test_deserialize_book_unsuccessfully(self):
        """
        Deserialize a category unsucessfully
        (Filling field with wrong data types)
        """

        serializer = CategorySerializer(data={"name": False})

        self.assertFalse(serializer.is_valid())
        self.assertTrue(bool(serializer.errors))


class AuthorSerializerTestCase(TestCase):

    def test_serialize_author_successfully(self):
        """
        Serialize an Author sucessfully
        """

        data = AUTHOR_ATTRS.copy()
        author = Author.objects.create(**data)
        serializer = AuthorSerializer(author)

        self.assertEqual(author.first_name, serializer.data["first_name"])
        self.assertEqual(author.second_name, serializer.data["second_name"])
        self.assertEqual(
            author.paternal_last_name, serializer.data["paternal_last_name"]
        )
        self.assertEqual(
            author.maternal_last_name, serializer.data["maternal_last_name"]
        )
        self.assertEqual(author.country, serializer.data["country"])

    def test_deserialize_author_sucessfully(self):
        """
        Deserialize an author sucessfully
        """

        data = AUTHOR_ATTRS.copy()
        serializer = AuthorSerializer(data=data)

        self.assertTrue(serializer.is_valid())
        self.assertEqual(
            serializer.validated_data["first_name"], AUTHOR_ATTRS["first_name"]
        )
        self.assertEqual(
            serializer.validated_data["second_name"], AUTHOR_ATTRS["second_name"]
        )
        self.assertEqual(
            serializer.validated_data["paternal_last_name"],
            AUTHOR_ATTRS["paternal_last_name"],
        )
        self.assertEqual(
            serializer.validated_data["maternal_last_name"],
            AUTHOR_ATTRS["maternal_last_name"],
        )
        self.assertEqual(serializer.validated_data["country"], AUTHOR_ATTRS["country"])
        self.assertFalse(bool(serializer.errors))

    def test_deserialize_author_unsucessfully(self):
        """
        Deserialize an author unsucessfully
        (empty payload)
        """

        serializer = AuthorSerializer(data={})

        self.assertFalse(serializer.is_valid())
        self.assertTrue(bool(serializer.errors))
