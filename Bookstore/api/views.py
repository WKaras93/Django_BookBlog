from rest_framework import generics, mixins
from shop.models import Book
from .serializers import BookSerializer
from .permissions import IsOwnerOrReadOnly

class BookAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    #permission_classes = []

    def perform_create(self, serializer):
        serializer.save(create=self.request.user)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}
    
    # def put(self, request, *args, **kwargs):
    #     return self.update(request, *args, **kwargs)
    
    # def patch(self, request, *args, **kwargs):
    #     return self.create(request, *args, **kwargs)

class BookRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = BookSerializer
    permission_classes = [IsOwnerOrReadOnly]
    #queryset = Book.objects.all()

    def get_queryset(self):
        return Book.objects.all()
    
    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}
    
    # def get_object(self):
    #     pk = self.kwargs.get("pk")
    #     return Book.objects.get(pk=pk)