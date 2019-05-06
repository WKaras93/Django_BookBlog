from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.forms import CheckboxSelectMultiple, ModelMultipleChoiceField, ModelForm

class Tag(models.Model):
    content = models.CharField(max_length = 100)

    def __str__(self):
        return self.content

class Book(models.Model):
    title = models.CharField(max_length = 100)
    author = models.CharField(max_length = 100)
    publisher = models.CharField(max_length = 100)
    publication_date = models.DateField()
    review = models.TextField()
    image = models.ImageField(default = 'defaultBook.jpg', upload_to = 'book_pics')
    create = models.ForeignKey(User, on_delete = models.CASCADE)
    tags = models.ManyToManyField('Tag')

    def __str__(self):
        return '%s %s' % (self.title, self.author) 
    
    def get_absolute_url(self):
        return reverse("book-detail", kwargs={"pk": self.pk})

class Post(models.Model):
    content = models.TextField()
    date_posted = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    book = models.ForeignKey(Book, on_delete = models.CASCADE)

    def get_absolute_url(self):
        return reverse("book-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.content