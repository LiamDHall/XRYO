from django.test import TestCase

# Create your tests here.


class TestBagViews(TestCase):

    def test_bag_get(self):
        """ Tests response and if template is correct
        """

        response = self.client.get('/bag/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bag/bag.html')
