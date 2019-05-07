from django.contrib import admin
from . models import Book, Comment, Tag


admin.site.register(Book)
admin.site.register(Comment)
admin.site.register(Tag)