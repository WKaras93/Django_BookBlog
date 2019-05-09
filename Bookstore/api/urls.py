from django.conf.urls import url
from .views import BookRudView

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', BookRudView.as_view(), name='book-rud'),
]