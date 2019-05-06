from django.urls import path
from . views import BookDetailView, BookCreateView, BookUpdateView, PostCreateView
from . import views # . means dir

urlpatterns = [
    path('', views.home, name = 'shop-home'),
    path('bookList', views.get_books, name = 'shop-home'),
    path('bookJson', views.bookJson, name = 'book-json'),
    path('book/<int:pk>', BookDetailView.as_view(), name = 'book-detail'),
    path('book/new/', BookCreateView.as_view(), name = 'book-create'),
    path('book/<int:pk>/update/', BookUpdateView.as_view(), name = 'book-update'),
    path('post/new/', PostCreateView.as_view(), name = 'post-create'),
    path('about/', views.about, name = 'shop-about')
]