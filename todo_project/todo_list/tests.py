from django.test import TestCase
from django.urls import reverse, resolve
from .models import Task
from . import views

# Create your tests here.

class homepageTests(TestCase):
    def setUp(self):
        Task.objects.create(title='test_task', description='test_task_description')
        self.url_path = reverse('homepage')
        self.response = self.client.get(self.url_path)
    
    def test_homepage_view_success_status(self):
        self.assertEqual(self.response.status_code, 200)
    
    def test_homepage_url_resolves_homepage_view(self):
        resolved_view = resolve("/")
        self.assertEqual(resolved_view.func, views.homepage)
    
    def test_homepage_contains_link_to_task_page(self):
        task_page_url = reverse(views.task_page, kwargs={'pk': 1})
        self.assertContains(self.response, 'href="{0}"'.format(task_page_url))
    
    def test_homepage_contains_link_to_new_task_page(self):
        new_task_url = reverse('new_task')
        self.assertContains(self.response, f'href="{new_task_url}"')


