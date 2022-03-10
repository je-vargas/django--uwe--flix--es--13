from django.contrib.auth import get_user_model
from django.test import TestCase, SimpleTestCase, Client
from django.urls import reverse
from .models import Film
import datetime

#! SimpleTestCase used instead of TestCase since we are not calling off to a DB

# class SimpleTests(SimpleTestCase):
#     def test_home_page_status_code(self):
#         response = self.client.get('/')
#         self.assertEqual(response.status_code, 200)

#     def test_about_page_status_code(self):
#         response = self.client.get('/about/')
#         self.assertEqual(response.status_code, 200)

class FilmTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(
            username='testUser',
            email='test@email.com',
            password='secret'
        )

        self.film = Film.objects.create(
            title='test film',
            age_rating='PG',
            duration='1hr 10mins',
            film_description='One of the best test case scenarios',
            release_date=datetime.date(2022, 3, 10)
        )

    def test_string_representation(self):
        film = Film(title='A marmite film')
        self.assertEqual(str(film), film.title)
        pass

    def test_post_content(self):
        date = str(datetime.date(2022, 3, 10))
        self.assertEqual(f"{self.film.title}", "test film")
        self.assertEqual(f"{self.film.age_rating}", "PG")
        self.assertEqual(f"{self.film.duration}", "1hr 10mins")
        self.assertEqual(f"{self.film.film_description}", "One of the best test case scenarios")
        self.assertEqual(f"{self.film.release_date}", date)
    
    def test_film_content(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'One of the best test case scenarios')
        self.assertTemplateUsed(response, 'web_app/home.html')

    def test_film_detail_view(self):
        response = self.client.get("/films/1/")
        no_response = self.client.get("/films/10000000000/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'test film')
        self.assertTemplateUsed(response, 'web_app/film_detail.html')
