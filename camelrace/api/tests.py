from django.test import TestCase, SimpleTestCase
# Create your tests here.
from .models import UserProfile


class HomePageTest(TestCase):

    def test_home_status_code(self):
        response = self.client.get('/api/racers/')
        self.assertEquals(response.status_code, 200)


class PostTests(TestCase):
    @classmethod
    def setUp(cls):
        UserProfile.objects.create(name='ahmed')

    def test_name(self):
        user = UserProfile.objects.get(id=1)
        expect_name = user.name
        self.assertEquals(expect_name, 'ahmed')
