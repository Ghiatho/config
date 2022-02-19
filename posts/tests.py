from django.test import TestCase
from django.urls import reverse
from .models import Post

# Create your tests here.

class PostModelTest(TestCase):
    def setUp(self):
        Post.objects.create(text='This is a test post from PostModelTest')           # create the content

    def test_text_content(self):                                                     # first test case
        post = Post.objects.get(id=1)
        expected_object_name = f'{post.text}'
        self.assertEqual(expected_object_name, 'This is a test post from PostModelTest')


class HomePageVeiwTest(TestCase):
    def setUp(self):
        Post.objects.create(text='This is a test post from PostModelTest')

    def test_view_url_exists_at_proper_location(self): # does homepage actually exist and return a HTTP 200 response?
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_by_name(self):                  #  does it use HomePageView as the view?
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):       # does it use home.html as the template?
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'posts/home.html')