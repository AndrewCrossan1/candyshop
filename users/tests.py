from django.test import TestCase

from users.models import User


# Create your tests here.
class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create_user(username='test',
                                 password='test',
                                 email='test@gmail.com',
                                 first_name='test',
                                 last_name='test')

    def test_user(self):
        user = User.objects.get(username='test')
        self.assertEqual(user.username, 'test')
