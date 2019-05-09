#Code without tests is broken as designed.
#                   Jacob Kaplan-Moss

from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Tag
from .serializer import TagSerializer

#test for views
class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_tag(content = ""):
        if content != "":
            Tag.objects.create(content = content)
    
    def setUp(self):
        self.create_tag("Literature & Fiction")
        self.create_tag("Arts & Music")
        self.create_tag("Biographies")
        self.create_tag("Business")

class GetAllTagTest(BaseViewTest):
    def test_get_all_tags(self):
        """ This test ensure that all song added in the setUp method exist when we make a GET request to tags"""
        
        response = self.client.get(
            reverse("tags-all", kwargs={"version": "v1"})
        )

        expected = Tag.objects.all()
        serialized = TagSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

