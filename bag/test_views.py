import random

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

    # Product Only to Bag
    def test_product_to_bag(self):
        """ Test product (without size or vairant) is added to bag and
        redirects back to correct product page.
        """

        # Create Product
        product = Product.objects.create(name='Test Product', price='10', rating='0', rating_total='0', no_of_ratings='0')

        # Add product to bag
        url = reverse('product_to_bag', kwargs={'product_id': product.id})
        current_page = f'/products/{product.id}'
        post_data = {'current_page': current_page}
        response = self.client.post(url, data=post_data)

        # Check if product in the bag and correctly formated
        session = self.client.session
        self.assertEqual(session['bag'], {f'{product.id}': 1})

        # Test Redirect
        self.assertRedirects(response, current_page)

    # Product with Variant to Bag
    def test_product_with_variant_to_bag(self):
        """ Test product with vairant (no size) is added to bag and
        redirects back to correct product page.
        """

        # Create Product & Vairant
        product = Product.objects.create(name='Test Product', price='10', rating='0', rating_total='0', no_of_ratings='0')
        variant = Variant.objects.create(name='Test Variant', product=product)

        # Add them to bag
        url = reverse('product_to_bag', kwargs={'product_id': product.id})
        current_page = f'/products/{product.id}/{variant.id}'
        post_data = {'current_page': current_page, 'product_variant': variant.id}
        response = self.client.post(url, data=post_data)

        # Check if they are in the bag and correctly formated
        product_bag_dict = {f'{product.id}': {'product_by_variant': {f'{variant.id}': 1}}}
        session = self.client.session
        self.assertEqual(session['bag'], product_bag_dict)

        # Test Redirect
        self.assertRedirects(response, current_page)

    # Product with Size to Bag
    def test_product_with_size_to_bag(self):
        """ Test product with size (no variant) is added to bag and
        redirects back to correct product page.
        """

        # Create Product with Size
        product = Product.objects.create(name='Test Product', sizes=True, price='10', rating='0', rating_total='0', no_of_ratings='0')

        # Add product to bag
        url = reverse('product_to_bag', kwargs={'product_id': product.id})
        current_page = f'/products/{product.id}'
        size = 'test_size'
        post_data = {'current_page': current_page, 'product_size': size}
        response = self.client.post(url, data=post_data)

        # Check if product with size in the bag and correctly formated
        product_bag_dict = {f'{product.id}': {'product_by_size': {f'{size}': 1}}}
        session = self.client.session
        self.assertEqual(session['bag'], product_bag_dict)

        # Test Redirect
        self.assertRedirects(response, current_page)

    # Product Only Quantity Change
    def test_update_bag_product_quantity(self):
        """ Test to see if the quantity of an product (without size or
        vairant) is increase when updated from the bag and redirects
        back to bag page
        """
        product = Product.objects.create(name='Test Product', price='10', rating='0', rating_total='0', no_of_ratings='0')

        # Add product to bag
        url = reverse('product_to_bag', kwargs={'product_id': product.id})
        current_page = f'/products/{product.id}'
        post_data = {'current_page': current_page}
        self.client.post(url, data=post_data)

        # Test quantity change
        quantity = random.randint(1, 10)
        post_data = {'quantity': quantity}
        url = reverse('update_bag', kwargs={'product_id': product.id})
        response = self.client.post(url, data=post_data)
        session = self.client.session
        self.assertEqual(session['bag'], {f'{product.id}': quantity})

        # Test Redirect
        self.assertRedirects(response, '/bag/')

    # Product with Variant Quantity Change
    def test_update_bag_product_with_variants_quantity(self):
        """ Test to see if the quantity of an product with variant
        (no size) is increase when updated from the bag and redirects
        back to bag page
        """
        product = Product.objects.create(name='Test Product', price='10', rating='0', rating_total='0', no_of_ratings='0')
        variant = Variant.objects.create(name='Test Variant', product=product)

        # Add product and its variant to bag
        url = reverse('product_to_bag', kwargs={'product_id': product.id})
        current_page = f'/products/{product.id}/{variant.id}'
        post_data = {'current_page': current_page, 'product_variant': variant.id}
        self.client.post(url, data=post_data)

        # Test quantity change
        quantity = random.randint(1, 10)
        post_data = {'quantity': quantity, 'product_variant': variant.id}
        url = reverse('update_bag', kwargs={'product_id': product.id})
        response = self.client.post(url, data=post_data)
        product_bag_dict = {f'{product.id}': {'product_by_variant': {f'{variant.id}': quantity}}}
        session = self.client.session
        self.assertEqual(session['bag'], product_bag_dict)

        # Test Redirect
        self.assertRedirects(response, '/bag/')

    # Product with Size Quantity Change
    def test_update_bag_product_with_size_quantity(self):
        """ Test to see if the quantity of an product (without size or
        vairant) is increase when updated from the bag and redirects
        back to bag page
        """
        product = Product.objects.create(name='Test Product', sizes=True, price='10', rating='0', rating_total='0', no_of_ratings='0')
        url = reverse('product_to_bag', kwargs={'product_id': product.id})
        current_page = f'/products/{product.id}'
        size = 'test_size'
        post_data = {'current_page': current_page, 'product_size': size}
        response = self.client.post(url, data=post_data)

        # Test quantity change
        quantity = random.randint(1, 10)
        post_data = {'quantity': quantity, 'product_size': size}
        url = reverse('update_bag', kwargs={'product_id': product.id})
        response = self.client.post(url, data=post_data)
        product_bag_dict = {f'{product.id}': {'product_by_size': {f'{size}': quantity}}}
        session = self.client.session
        self.assertEqual(session['bag'], product_bag_dict)

        # Test Redirect
        self.assertRedirects(response, '/bag/')
