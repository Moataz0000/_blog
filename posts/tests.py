from django.test import TestCase
from posts.models import Post
# Create your tests here.



class PostModelTest(TestCase):
    def setUp(self):
        self.post = Post.objects.create(
            title='Test Title',
            content='Test Content'
        )

    def test_post_creation(self):
        post = Post.objects.get(id=1)
        self.assertEqual(post.title, 'Tesst Title')
        self.assertEqual(post.content, 'Test Content')
        self.assertTrue(isinstance(post, Post))
