from django.contrib.auth import get_user_model
from core import models
from datetime import datetime
from django.db import utils
from django.test import TestCase


class UserModelTestCase(TestCase):
    """
    User Model tests
    """

    def test_create_user_successfully(self):
        """
        Create a new user successfully
        """

        User = get_user_model()
        username = "mrfixthis"
        email = "mrfixthis@gmail.com"
        password = "testpassword"
        first_name = "Bryan"
        paternal_last_name = "Baron"

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            paternal_last_name=paternal_last_name
        )

        self.assertEquals(user.username, username)
        self.assertEquals(user.email, email)
        self.assertEquals(user.first_name, first_name)
        self.assertEquals(user.paternal_last_name, paternal_last_name)
        self.assertNotEqual(user.password, password)
        self.assertTrue(user.check_password(password))
        self.assertEqual(user.second_name, "")
        self.assertEqual(user.maternal_last_name, "")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertEqual(user.picture, None)

    def test_create_user_unsuccessfully(self):
        """
        Create a new user unsuccessfully
        (setting too long field values)
        """

        User = get_user_model()
        username = "mrfixthis" * 20
        email = "mrfixthis@gmail.com" * 20
        password = "testpassword" * 20
        first_name = "Bryan" * 20
        paternal_last_name = "Baron" * 20

        with self.assertRaises(utils.DataError):
            User.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name=first_name,
                paternal_last_name=paternal_last_name
            )

    def test_user_email_is_normalized(self):
        """
        Check if the user email is normalized correctly
        """

        User = get_user_model()
        email = "test@Normalization.com"
        user = User.objects.create_user(
          username="username",
          first_name="user_test",
          paternal_last_name="paternal_last_name_test",
          password="passwd",
          email=email
        )
        self.assertEqual(user.email, email.lower())

    def test_str_representation_is_username(self):
        """
        Check if str reprentation is the user name
        """

        User = get_user_model()
        username="test_user_name"
        user = User(username=username)
        self.assertEqual(str(user), username)

    def test_fullname_is_names_and_last_names(self):
        """
        Check if the full name is the first_name, second_name,
        paternal_last_name, maternal_last_name together
        """

        User = get_user_model()
        user_attrs = {
            "first_name": "Axel",
            "second_name": "Alberto",
            "paternal_last_name": "Mora",
            "maternal_last_name": "Rico"
        }
        fullname = " ".join(user_attrs.values())
        user = User(**user_attrs)
        self.assertEqual(user.get_full_name(), fullname)

    def test_short_name_is_first_name_and_paternal_last_name(self):
        """
        Check if the short name is the first_name
        and paternal_last_name together
        """

        User = get_user_model()
        user_attrs = {
            "first_name": "Axel",
            "paternal_last_name": "Mora",
        }
        short_name = " ".join(user_attrs.values())
        user = User(**user_attrs)
        self.assertEqual(user.get_short_name(), short_name)


class CategoryModelTestCase(TestCase):
    """
    Category Model tests
    """

    def test_create_category_successfully(self):
        """
        Create a new Category successfully
        """

        category_name = "Action"
        category = models.Category(name=category_name)
        category.save()

        self.assertEqual(category.name, category_name)
        self.assertIsInstance(category.time_stamp, datetime)

    def test_create_category_unsuccessfully(self):
        """
        Create a new Category unsuccessfully
        (too long field values)
        """

        category_name = "Action" * 20
        with self.assertRaises(utils.DataError):
            category = models.Category(name=category_name)
            category.save()

    def test_str_representation_is_name(self):
        """
        Check if str reprentation is the category name
        """
        category_name = "Action"
        category = models.Category(name=category_name)
        category.save()

        self.assertEqual(str(category), category_name)

class BookModelTestCase(TestCase):
    """
    Book model tests
    """

    def test_create_book_successfully(self):
        """
        Create new book successfully
        """

        title = "Python The Hard Way"
        description = "Python book"
        edition = "9.8F"
        language = "English"
        page_number = 350
        publishier = "PubTest"

        book = models.Book(
            title=title,
            description=description,
            edition=edition,
            language=language,
            page_number=page_number,
            publishier=publishier,
        )
        book.save()

        self.assertEqual(book.title, title)
        self.assertEqual(book.description, description)
        self.assertEqual(book.edition, edition)
        self.assertEqual(book.language, language)
        self.assertEqual(book.page_number, page_number)
        self.assertEqual(book.publishier, publishier)
        self.assertTrue(book.available)
        self.assertEqual(book.rating, 8.0)
        self.assertIsInstance(book.time_stamp, datetime)

    def test_create_book_unsuccessfully(self):
        """
        Create a new Book unsuccessfully
        (too long field values)
        """

        title = "Python The Hard Way" * 20
        description = "Python book"

        with self.assertRaises(utils.DataError):
            book = models.Book(
                title=title,
                description=description
            )
            book.save()

    def test_book_rating_range_exceeded(self):
        """
        Check if book rating is greater than 1.0 but less than 10.0
        """

        title = "VimScript the Hard Way"
        rating = 13.2

        with self.assertRaises(utils.IntegrityError):
            book = models.Book(
                title=title,
                rating=rating
            )
            book.save()

    def test_str_representation_is_title(self):
        """
        Check if the str reprentation is the book title
        """

        title = "Java Complete Edition"
        book = models.Book(title=title)
        book.save()

        self.assertEqual(str(book), title)

class ShoppingCartModelTestCase(TestCase):
    """
    ShoppingCart model tests
    """

    def test_create_shopping_cart_successfully(self):
        """
        Create a new shopping cart successfully
        """

        User = get_user_model()
        user_attrs = {
            "username": "KraSpar",
            "email": "kratoss@olimpo.com",
            "password": "ZeusSucks",
            "first_name": "Kratos",
            "paternal_last_name": "Sparta",
        }
        user = User.objects.create_user(**user_attrs)
        user.save()

        book_attrs = {
            "title": "Clean Code",
            "description": "Clean code book description",
            "edition": "10T",
            "language": "English",
            "page_number": 800,
            "publishier": "pubName",
        }
        book = models.Book(**book_attrs)
        book.save()

        cart = models.ShoppingCart(user=user)
        cart.save()
        cart.books.add(book)
        cart.save()

        self.assertEqual(cart.user, user)
        self.assertEqual(cart.books.first(), book)
        self.assertIsInstance(cart.time_stamp, datetime)


class AuthorModelTestCase(TestCase):
    """
    Author Model tests
    """

    def test_create_author_successfully(self):
        """
        Create a now autor successfully
        """

        first_name = "Gabriel"
        second_name = "Jose"
        paternal_last_name = "Garcia"
        maternal_last_name = "Marquez"
        country = "Colombia"

        author = models.Author(
            first_name=first_name,
            second_name=second_name,
            paternal_last_name=paternal_last_name,
            maternal_last_name=maternal_last_name,
            country=country
        )
        author.save()

        book_attrs = {
            "title": "Data Strutures and Algos",
            "description": "book desc",
            "edition": "8n",
            "language": "Spanish",
            "page_number": 700,
            "publishier": "publishierName",
        }
        book = models.Book(**book_attrs)
        book.save()

        author.books.add(book)

        self.assertEqual(author.first_name, first_name)
        self.assertEqual(author.second_name, second_name)
        self.assertEqual(author.paternal_last_name, paternal_last_name)
        self.assertEqual(author.maternal_last_name, maternal_last_name)
        self.assertEqual(author.country, country)
        self.assertEqual(author.books.first(), book)
        self.assertIsInstance(author.time_stamp, datetime)
        self.assertEqual(author.picture, None)

    def test_create_author_unsuccessfully(self):
        """
        Create a new author unsuccessfully
        (too long field values)
        """

        first_name = "Gabriel" * 40
        paternal_last_name = "Garcia" * 40
        country = "Colombia" * 40

        with self.assertRaises(utils.DataError):
            author = models.Author(
                first_name=first_name,
                paternal_last_name=paternal_last_name,
                country=country
            )
            author.save()

    def test_str_representation_is_first_name(self):
        """
        Check if str reprentation is author frist name
        """

        first_name = "Julio"
        paternal_last_name = "Cortazar"
        country = "Argentine"

        author = models.Author(
            first_name=first_name,
            paternal_last_name=paternal_last_name,
            country=country
        )
        author.save()

        self.assertEqual(str(author), first_name)

    def test_short_name_is_first_name_and_paternal_last_name(self):
        """
        Check if the short name is the first_name
        and paternal_last_name together
        """

        first_name = "Fernando"
        paternal_last_name = "Aparicio"
        country = "Colombia"
        short_name = "{0} {1}".format(first_name, paternal_last_name)

        author = models.Author(
            first_name=first_name,
            paternal_last_name=paternal_last_name,
            country=country
        )
        author.save()

        self.assertEqual(short_name, author.get_short_name())
