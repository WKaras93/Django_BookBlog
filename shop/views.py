from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import DetailView, CreateView, UpdateView
from . models import Book, Post
    
def home(request):
    context = {
        'books': Book.objects.all()
    }
    return render(request, 'shop/home.html', context)

class BookDetailView(DetailView):
    model = Book

class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    fields = ['title', 'author', 'publisher', 'publication_date', 'review', 'image']
    
    def form_valid(self, form):
        form.instance.create = self.request.user
        return super().form_valid(form)

class BookUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Book
    fields = ['title', 'author', 'publisher', 'publication_date', 'review', 'image']

    def form_valid(self, form):
        form.instance.create = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        book = self.get_object()
        if self.request.user == book.create:
            return True
        return False

def about(request):
    return render(request, 'shop/about.html')