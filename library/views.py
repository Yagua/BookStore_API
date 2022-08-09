from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .serializers import BookSerializer, CategorySerializer
from core.models import Book, Category
from rest_framework.response import Response
from rest_framework import status

class BookList(APIView):
    """
    BookList View
    List all books in database or create new one
    """

    def get(self, request):
        """
        Get all books in database
        """

        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
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
    BookDetail View
    Get an specific book, update, or delete it
    """

    def get_object(self, pk):
        """
        Get a book object or return '404 Not Found' message
        if it does not exists in database
        """

        try:
            return Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return Response(
                    {"message": f"Book identified with 'pk: {pk}' not found"},
                    status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        """
        Get a book by id (primary key)
        """

        book = self.get_object(pk)
        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        """
        Update an specific book
        """

        book = self.get_object(pk)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def patch(self, request, pk):
        """
        Update partially an specific book
        """

        book = self.get_object(pk)
        serializer = BookSerializer(book, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """
        Delete a book
        """

        book = self.get_object(pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["GET"])
def book_categories(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return Response(
                {"message": f"Book identified with 'pk: {pk}' not found"},
                status=status.HTTP_404_NOT_FOUND)
    book_categories = book.categories
    serializer = CategorySerializer(book_categories, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


class CategoryList(APIView):
    """
    CategoryList View
    List all categories in database or create new one
    """

    def get(self, request):
        """
        Get all categories in database
        """

        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
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
    CategoryDetail View
    Get an specific category, update, or delete it
    """

    def get_object(self, pk):
        """
        Get a category object or return '404 Not Found' message
        if it does not exists in database
        """

        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response(
                    {"message": f"Category identified with 'pk: {pk}' not found"},
                    status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        """
        Get a category by id (primary key)
        """

        category = self.get_object(pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        """
        Update an specific category
        """

        category = self.get_object(pk)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        """
        Update partially an specific category
        """

        category = self.get_object(pk)
        serializer = CategorySerializer(category, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """
        Delete a category
        """

        category = self.get_object(pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
