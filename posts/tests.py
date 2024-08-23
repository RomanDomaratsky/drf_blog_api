from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Post


# Create your tests here.
class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret',
        )

        cls.post = Post.objects.create(
            author=cls.user,
            title='Test title',
            body='Test body',
        )

    def test_post_model(self):
        self.assertEqual(self.post.author.username, 'testuser')
        self.assertEqual(self.post.title, 'Test title')
        self.assertEqual(self.post.body, 'Test body')
        self.assertEqual(str(self.post), 'Test title')
