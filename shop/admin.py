from django.contrib import admin
from . models import Book, Post, Tag


admin.site.register(Book)
admin.site.register(Post)
admin.site.register(Tag)