from django.test import TestCase
from .models import Post

# Create your tests here.

class PostModelTest(TestCase):
    test_string = "Hello world, test post"

    def setUp(self):
        # Set up a post object for testing
        self.post = Post.objects.create(body=self.test_string)

    def test_post_creation(self):
        # Check that the post is created correctly
        self.assertEqual(self.post.body, self.test_string)
        self.assertTrue(self.post.create_date)  # Check if date field is filled