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
        """ Test product (without size or vairant) is added to bag and
        redirects back to correct product page.
        """

        product = Product.objects.create(name='Test Product', price='10', rating='0', rating_total='0', no_of_ratings='0')
        url = reverse('product_to_bag', kwargs={'product_id': product.id})
        current_page = f'/products/{product.id}'
        post_data = {'current_page': current_page}
        response = self.client.post(url, data=post_data)
        self.assertRedirects(response, current_page)
        session = self.client.session
        self.assertEqual(session['bag'], {f'{product.id}': 1})

    def test_product_with_variant_to_bag(self):
        """ Test product with vairant (no size) is added to bag and
        redirects back to correct product page.
        """
        product = Product.objects.create(name='Test Product', price='10', rating='0', rating_total='0', no_of_ratings='0')
        variant = Variant.objects.create(name='Test Variant', product=product)
        url = reverse('product_to_bag', kwargs={'product_id': product.id})
        current_page = f'/products/{product.id}/{variant.id}'
        post_data = {'current_page': current_page, 'product_variant': variant.id}
        response = self.client.post(url, data=post_data)
        product_bag_dict = {f'{product.id}': {'product_by_variant': {f'{variant.id}': 1}}}
        self.assertRedirects(response, current_page)
        session = self.client.session
        self.assertEqual(session['bag'], product_bag_dict)

    def test_product_with_size_to_bag(self):
        """ Test product with size (no variant) is added to bag and
        redirects back to correct product page.
        """
        product = Product.objects.create(name='Test Product', sizes=True, price='10', rating='0', rating_total='0', no_of_ratings='0')
        url = reverse('product_to_bag', kwargs={'product_id': product.id})
        current_page = f'/products/{product.id}'
        size = 'test_size'
        post_data = {'current_page': current_page, 'product_size': size}
        response = self.client.post(url, data=post_data)
        product_bag_dict = {f'{product.id}': {'product_by_size': {f'{size}': 1}}}
        self.assertRedirects(response, current_page)
        session = self.client.session
        self.assertEqual(session['bag'], product_bag_dict)
