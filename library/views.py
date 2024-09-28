from library.models import  Book, BookTracker


from rest_framework import viewsets

from library.serializers import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer



