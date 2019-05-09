from rest_framework import generics
from shop.models import Book
from .serializers import BookSerializer

class BookRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = BookSerializer
    queryset = Book.objects.all()

    def get_queryset(self):
        return Book.objects.all()
    
    # def get_object(self):
    #     pk = self.kwargs.get("pk")
    #     return Book.objects.get(pk=pk)