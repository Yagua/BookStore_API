from django.db import models
from django.db.models import Q
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin, BaseUserManager
)

def get_path(instance, filename):
    return "user_{0}/{1}".format(instance.username, filename)

class UserManager(BaseUserManager):
    def create_user(self, username, email, password,
            first_name, paternal_last_name, **extra_fields):

        user = self.model(
            username=username,
            email=self.normalize_email(email),
            first_name=first_name,
            paternal_last_name=paternal_last_name,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """
    Custom User model
    """

    username = models.CharField(max_length=150, unique=True)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=128)
    first_name = models.CharField(max_length=150)
    second_name = models.CharField(max_length=150, blank=True)
    paternal_last_name = models.CharField(max_length=150)
    maternal_last_name = models.CharField(max_length=150, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    picture = models.ImageField(upload_to=get_path, blank=True, null=True)

    objects = UserManager()

    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = []

    def get_full_name(self):
        """
        Get full user name
        """

        return "{0} {1} {2} {3}".format(self.first_name, self.second_name,
                self.paternal_last_name, self.maternal_last_name)

    def get_short_name(self):
        """
        Get short user name
        """

        return "{0} {1}".format(self.first_name, self.paternal_last_name)

    class Meta:
        db_table = "user"

    def __str__(self):
        return self.username


class Category(models.Model):
    """
    Category model
    """

    name = models.CharField(max_length=50)
    time_stamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "category"

    def __str__(self):
        return self.name

class Book(models.Model):
    """
    Book model
    """

    title = models.CharField(max_length=80)
    description = models.TextField(max_length=200)
    cover = models.ImageField(upload_to="books/", blank=True, null=True)
    edition = models.CharField(max_length=50)
    language = models.CharField(max_length=80)
    page_number = models.IntegerField(default=0)
    publishier = models.CharField(max_length=100)
    rating = models.FloatField(default=8.0)
    available = models.BooleanField(default=True)
    categories = models.ManyToManyField(Category, related_name="books")
    time_stamp = models.DateTimeField(auto_now_add=True)

    # def get_categories_as_str(self):
    #     return ", ".join([category.name for category in self.categories.all()])

    class Meta:
        db_table = "book"
        constraints = [
            models.CheckConstraint(
                check=Q(rating__gte=1.0) & Q(rating__lte=10.0),
                name="rating_gte_1.0_and_lte_10.0"
            )
        ]

    def __str__(self):
        return self.title

class ShoppingCart(models.Model):
    """
    ShoppingCart model
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    books = models.ManyToManyField(Book, "carts")
    time_stamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "shopping_cart"

class Author(models.Model):
    """
    Author model
    """

    first_name = models.CharField(max_length=80)
    second_name = models.CharField(max_length=80)
    paternal_last_name = models.CharField(max_length=80)
    maternal_last_name = models.CharField(max_length=80)
    picture = models.ImageField(upload_to="book_authors/", null=True, blank=True)
    country = models.CharField(max_length=70)
    books = models.ManyToManyField(Book, related_name="authors")
    time_stamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "author"

    def get_short_name(self):
        return "%s %s" % (self.first_name, self.paternal_last_name)

    def __str__(self):
        return self.first_name