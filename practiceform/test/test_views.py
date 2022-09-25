from urllib import response
from django.test import TestCase, Client
from django.urls import reverse
from practiceform.models import Post, PostCategory
import json


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.list_url = reverse('home')
        self.detail_url=reverse('post', args=['2'])
        self.post1=Post.objects.create(id=2,
                            title='work',
                            content='lets go to work'
                            )

    def test_post_list_GET(self):
        response=self.client.get(self.list_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'practiceform/home.html')

    def test_post_detail_GET(self):
        response=self.client.get(self.detail_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'practiceform/post.html')