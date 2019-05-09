from rest_framework import serializers
from shop.models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publisher', 'publication_date', 'review', 'image', 'tags']
    
    #For this example, it doesn't make sense, because there are books with the same titles by different authors, but I leave for example
    def validate_title(self, value):
        qs = Book.objects.filter(title__iexact=value)
        if qs.exists():
            raise serializers.ValidationError("The title must be unique")
        return value