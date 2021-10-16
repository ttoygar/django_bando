from django.test import TestCase
from lp.views import landing_page
from django.urls import resolve


class LandingTest(TestCase):

    def test_root_resolves_to_landing_page_view(self):
        page = resolve('/')
        self.assertEqual(page.func, landing_page)
