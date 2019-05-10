from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from shop.models import Book
from rest_framework.reverse import reverse as api_reverse
from rest_framework import status


User = get_user_model()

class BookAPITestCase(APITestCase):
    def setUp(self):
        user_obj = User(username = 'TestUser5', email='TestUser5@mail.com')
        user_obj.set_password("PasswordTestUser")
        user_obj.save()
        book = Book.objects.create(
            title='The Three Musketeers',
            author='Vintage Dumas',
            publisher='PP',
            publication_date='1990-02-02',
            review='Situated between 1625 and 1628, it recounts the adventures of a young man named DArtagnan (based on Charles de Batz-Castelmore dArtagnan) after he leaves home to travel to Paris, to join the Musketeers of the Guard. Although dArtagnan is not able to join this elite corps immediately, he befriends the three most formidable musketeers of the age – Athos, Porthos and Aramis, the three inseparables as these are called – and gets involved in affairs of the state and court. ',
            create=user_obj,
            )
    
    def test_single_user(self):
        user_count = User.objects.count()
        self.assertEqual(user_count, 1)
    
    def test_single_post(self):
        book_count = Book.objects.count()
        self.assertEqual(book_count, 1)
    
    def test_get_item(self):
        data = {}
        url = api_reverse("api-booking:book-json-create")
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)