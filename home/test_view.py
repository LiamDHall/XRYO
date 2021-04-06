from django.test import TestCase

# Create your tests here.


class TestHomeView(TestCase):

    def test_homepage_get(self):
        """ Tests response and if template is correct
        """

        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')
