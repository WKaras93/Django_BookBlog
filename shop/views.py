from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import DetailView, CreateView, UpdateView
from .models import Book, Comment, Tag
from django.core import serializers
from django.http import HttpResponse
from .forms import CommentForm
from .serializer import TagSerializer
from rest_framework import generics

def home(request):
    context = {
        'books': Book.objects.all()
    }
    return render(request, 'shop/home.html', context)

def get_books(request):
    books = serializers.serialize('json', Book.objects.all())
    return HttpResponse(books, content_type = 'application/json')

def add_comment_to_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.book = book
            comment.author = request.user
            comment.save()
            return redirect('book-detail', pk=book.id)
    else:
        form = CommentForm()
    return render(request, 'shop/add_comment_to_book.html', {'form': form})

class BookDetailView(DetailView):
    model = Book

class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    fields = ['title', 'author', 'publisher', 'publication_date', 'review', 'image', 'tags']
    
    def form_valid(self, form):
        form.instance.create = self.request.user
        return super().form_valid(form)

class BookUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Book
    fields = ['title', 'author', 'publisher', 'publication_date', 'review', 'image', 'tags']

    def form_valid(self, form):
        form.instance.create = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        book = self.get_object()
        if self.request.user == book.create:
            return True
        return False

class ListTagView(generics.ListAPIView):
    """ Provides a get method handler """
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

def about(request):
    return render(request, 'shop/about.html')

def bookJson(request):
    return render(request, 'shop/bookJson.html')