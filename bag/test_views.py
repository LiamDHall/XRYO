from django.test import TestCase
from django.shortcuts import reverse
from products.models import Product, Variant

# Create your tests here.


class TestBagViews(TestCase):

    def test_view_bag(self):
        """ Tests response and if template is correct
        """

        response = self.client.get('/bag/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bag/bag.html')

    def test_product_to_bag(self):
        """ Test product is added to bag and redirects back to
        product page.
        """

        product = Product.objects.create(name='Test Product', price='10', rating='0', rating_total='0', no_of_ratings='0')
        url = reverse('product_to_bag', kwargs={'product_id': product.id})
        current_page = f'/products/{product.id}'
        post_data = {'current_page': current_page}
        response = self.client.post(url, data=post_data)
        self.assertRedirects(response, current_page)

    def test_variant_to_bag(self):
        """ Test product variant is added to bag and redirects back to
        product page.
        """

        product = Product.objects.create(name='Test Product', price='10', rating='0', rating_total='0', no_of_ratings='0')
        variant = Variant.objects.create(name='Test Variant', product=product)
        url = reverse('product_to_bag', kwargs={'product_id': product.id})
        current_page = f'/products/{product.id}/{variant.id}'
        post_data = {'current_page': current_page, 'variant_id': variant.id}
        response = self.client.post(url, data=post_data)
        self.assertRedirects(response, current_page)
