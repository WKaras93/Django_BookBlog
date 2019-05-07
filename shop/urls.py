from django.urls import path
from . views import BookDetailView, BookCreateView, BookUpdateView
from . import views # . means dir

urlpatterns = [
    path('', views.home, name = 'shop-home'),
    path('bookList', views.get_books, name = 'shop-home'),
    path('bookJson', views.bookJson, name = 'book-json'),
    path('book/<int:pk>', BookDetailView.as_view(), name = 'book-detail'),
    path('book/new/', BookCreateView.as_view(), name = 'book-create'),
    path('book/<int:pk>/update/', BookUpdateView.as_view(), name = 'book-update'),
    path('book/<int:pk>/comment/', views.add_comment_to_book, name='comment-create'),
    path('about/', views.about, name = 'shop-about')
]