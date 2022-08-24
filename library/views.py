from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from .serializers import BookSerializer, CategorySerializer, AuthorSerializer
from core.models import Book, Category, Author
from utils.model_tools import get_instance


class BookList(APIView):
    """
    List all books in database or create new one
    """

    def get(self, request):
        """
        Get all books in database
        """

        queryset = Book.objects.all()
        serializer = BookSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """
        Create a new book
        """

        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookDetail(APIView):
    """
    Get an specific book, update, or delete it
    """

    def get(self, request, pk):
        """
        Get a book by id (primary key)
        """

        exists, result = get_instance(Book, pk=pk)
        if not exists:
            return result

        serializer = BookSerializer(result)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        """
        Update an specific book
        """

        exists, result = get_instance(Book, pk=pk)
        if not exists:
            return result

        serializer = BookSerializer(result, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        """
        Update partially an specific book
        """

        exists, result = get_instance(Book, pk=pk)
        if not exists:
            return result

        serializer = BookSerializer(result, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """
        Delete a book
        """

        exists, result = get_instance(Book, pk=pk)
        if not exists:
            return result

        result.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["GET"])
def book_categories(request, pk):
    """
    Get all categories of the book specified by the given pk
    """

    exists, result = get_instance(Book, pk=pk)
    if not exists:
        return result

    categories = Category.objects.filter(books=result)
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


class CategoryList(APIView):
    """
    List all categories in database or create new one
    """

    def get(self, request):
        """
        Get all categories in database
        """

        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """
        Create a new category
        """

        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryDetail(APIView):
    """
    Get an specific category, update, or delete it
    """

    def get(self, request, pk):
        """
        Get a category by id (primary key)
        """

        exists, result = get_instance(Category, pk=pk)
        if not exists:
            return result

        serializer = CategorySerializer(result)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        """
        Update an specific category
        """

        exists, result = get_instance(Category, pk=pk)
        if not exists:
            return result

        serializer = CategorySerializer(result, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        """
        Update partially an specific category
        """

        exists, result = get_instance(Category, pk=pk)
        if not exists:
            return result

        serializer = CategorySerializer(
            result, data=request.data, partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """
        Delete a category
        """

        exists, result = get_instance(Category, pk=pk)
        if not exists:
            return result
        result.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["GET"])
def category_books(request, pk):
    """
    Get all books with the category specified by the given pk
    """

    exists, result = get_instance(Category, pk=pk)
    if not exists:
        return result
    books = Book.objects.filter(categories=result)
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


class AuthorList(APIView):
    """
    List all authors in database or create new one
    """

    def get(self, request):
        """
        Get all authors in database
        """

        queryset = Author.objects.all()
        serializer = AuthorSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """
        Create a new author
        """

        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AuthorDetail(APIView):
    """
    Get an specific author, update, or delete it
    """

    def get(self, request, pk):
        """
        Get an author by id (primary key)
        """

        exists, result = get_instance(Author, pk=pk)
        if not exists:
            return result

        serializer = AuthorSerializer(result)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        """
        Update an specific author
        """

        exists, result = get_instance(Author, pk=pk)
        if not exists:
            return result

        serializer = AuthorSerializer(result, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        """
        Update partially an specific author
        """

        exists, result = get_instance(Author, pk=pk)
        if not exists:
            return result

        serializer = AuthorSerializer(result, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """
        Delete an author
        """

        exists, result = get_instance(Author, pk=pk)
        if not exists:
            return result
        result.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["GET"])
def author_books(request, pk):
    """
    Get all books of the author specified by the given pk
    """

    exists, result = get_instance(Author, pk=pk)
    if not exists:
        return result

    books = Book.objects.filter(author=result)
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
