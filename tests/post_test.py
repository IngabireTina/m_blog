import unittest
from app.models import Blog, User,
from app import db


class BlogModelTest(unittest.TestCase):
    def setUp(self):
        self.user_tina = User(username='tina', password='tina', email='tina@gmail.com')
        self.new_blog = Blog(id=1, title='Test', post='post', user_id=self.user_tina.id)

    def tearDown(self):
        Blog.query.delete()
        User.query.delete()

    def test_check_instance_variables(self):
        self.assertEquals(self.new_blog.title, 'title')
        self.assertEquals(self.new_blog.post, 'post')
        self.assertEquals(self.new_blog.user_id, self.user_tina.id)

    def test_save_blog(self):
        self.new_blog.save()
        self.assertTrue(len(Blog.query.all()) > 0)

    def test_get_blog(self):
        self.new_blog.save()
        got_blog = Blog.get_blog(1)
        self.assertTrue(get_blog is not None)