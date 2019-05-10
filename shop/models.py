from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.forms import CheckboxSelectMultiple, ModelMultipleChoiceField, ModelForm
from rest_framework.reverse import reverse as api_reverse

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
    
    def get_api_url(self, request=None):
        return api_reverse("api-booking:book-rud", kwargs={"pk": self.pk}, request=request)
    
    @property
    def owner(self):
        return self.create

class Comment(models.Model):
    content = models.TextField()
    date_comment = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    book = models.ForeignKey(Book, on_delete = models.CASCADE, related_name='comments')
    approved_comment = models.BooleanField(default=False)
  
    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.content