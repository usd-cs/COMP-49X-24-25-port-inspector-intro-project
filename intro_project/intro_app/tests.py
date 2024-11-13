from django.test import TestCase
from django.contrib.auth.hashers import check_password
from intro_app.models import User, Post, Comment

class UserModelTest(TestCase):
	
	def setUp(self):
		# Set up a user instance for testing
		self.user = User.objects.create(email="testuser@example.com", name="Test User")
	
	def test_user_creation(self):
		self.assertEqual(self.user.email, "testuser@example.com")
		self.assertEqual(self.user.name, "Test User")
	
	def test_set_password(self):
		# Test the set_password method
		self.user.set_password("newpassword")
		self.user.refresh_from_db()  # Refresh the instance from the database to get the updated password
		self.assertTrue(check_password("newpassword", self.user.password))  # Check if the new password is hashed correctly
		
	def test_check_password(self):
		# Test the check_password method
		self.user.set_password("testpassword")
		self.assertTrue(self.user.check_password("testpassword"))  # Test the original password
		self.assertFalse(self.user.check_password("wrongpassword"))  # Test a wrong password


class PostModelTest(TestCase):

    def setUp(self):
        # Set up a user and a post instance for testing
        self.user = User.objects.create(email="testuser@example.com", name="Test User", password="testpassword")
        self.post = Post.objects.create(contents="This is a test post", user=self.user)

    def test_post_creation(self):
        # Check that the post is created correctly
        self.assertEqual(self.post.contents, "This is a test post")
        self.assertEqual(self.post.user, self.user)  # Check if the post is related to the correct user
        self.assertTrue(self.post.created_at)  # Check if created_at is set


class CommentModelTest(TestCase):

    def setUp(self):
        # Set up a user, a post, and a comment instance for testing
        self.user = User.objects.create(email="testuser@example.com", name="Test User", password="testpassword")
        self.post = Post.objects.create(contents="This is a test post", user=self.user)
        self.comment = Comment.objects.create(contents="This is a test comment", user=self.user, post=self.post)

    def test_comment_creation(self):
        # Check that the comment is created correctly
        self.assertEqual(self.comment.contents, "This is a test comment")
        self.assertEqual(self.comment.user, self.user)  # Check if the comment is related to the correct user
        self.assertEqual(self.comment.post, self.post)  # Check if the comment is related to the correct post
        self.assertTrue(self.comment.created_at)  # Check if created_at is set


class UserPostCommentTest(TestCase):

    def setUp(self):
        # Set up users, posts, and comments for relational tests
        self.user1 = User.objects.create(email="user1@example.com", name="User One", password="password1")
        self.user2 = User.objects.create(email="user2@example.com", name="User Two", password="password2")
        self.post = Post.objects.create(contents="Post by User One", user=self.user1)
        self.comment1 = Comment.objects.create(contents="Comment by User One", user=self.user1, post=self.post)
        self.comment2 = Comment.objects.create(contents="Comment by User Two", user=self.user2, post=self.post)

    def test_user_posts_relationship(self):
        # Ensure that the user has the correct posts related
        self.assertIn(self.post, self.user1.posts.all())  # Ensure post is listed under user1's posts
        self.assertEqual(self.post.user, self.user1)  # Ensure post is linked to the correct user

    def test_post_comments_relationship(self):
        # Ensure that the post has the correct comments related
        self.assertIn(self.comment1, self.post.comments.all())  # Ensure comment1 is related to post
        self.assertIn(self.comment2, self.post.comments.all())  # Ensure comment2 is related to post

    def test_user_comments_relationship(self):
        # Ensure that user1 has the correct comments related
        self.assertIn(self.comment1, self.user1.comments.all())  # Ensure comment1 is related to user1
        self.assertIn(self.comment2, self.user2.comments.all())  # Ensure comment2 is related to user2

# Create your tests here.