from django.conf.urls import url
from .views import BookRudView, BookAPIView

urlpatterns = [
    url(r'^$', BookAPIView.as_view(), name='book-json-create'),
    url(r'^(?P<pk>\d+)/$', BookRudView.as_view(), name='book-rud'),
]