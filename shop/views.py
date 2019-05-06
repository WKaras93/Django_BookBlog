from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import DetailView, CreateView, UpdateView
from . models import Book, Post, Tag
from django.core import serializers
from django.http import HttpResponse

def home(request):
    context = {
        'books': Book.objects.all()
    }
    return render(request, 'shop/home.html', context)

def get_books(request):
    books = serializers.serialize('json', Book.objects.all())
    return HttpResponse(books, content_type = 'application/json')

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

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['content', 'book']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

def about(request):
    return render(request, 'shop/about.html')

def bookJson(request):
    return render(request, 'shop/bookJson.html')