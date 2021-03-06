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
        product = Product.objects.create(
            name='Test Product',
            price='10', rating='0',
            rating_total='0',
            no_of_ratings='0'
        )

        # Add product to bag
        url = reverse('product_to_bag', kwargs={'product_id': product.id})
        current_page = f'/products/{product.id}'
        post_data = {'current_page': current_page}
        response = self.client.post(url, data=post_data)

        # Check if product in the bag and correctly formated
        session = self.client.session
        self.assertEqual(session['bag'], {f'{product.id}': 1})

        # Add product again
        self.client.post(url, data=post_data)

        # Check if 2 of the product are in the bag
        session = self.client.session
        self.assertEqual(session['bag'], {f'{product.id}': 2})

        # Test Redirect
        self.assertRedirects(response, current_page)

    # Product with Variant to Bag
    def test_product_with_variant_to_bag(self):
        """ Test product with vairant (no size) is added to bag and
        redirects back to correct product page.
        """

        # Create Product & Vairant
        product = Product.objects.create(
            name='Test Product',
            price='10',
            rating='0',
            rating_total='0',
            no_of_ratings='0'
        )
        variant_one = Variant.objects.create(
            name='Test Variant One',
            product=product
        )
        variant_two = Variant.objects.create(
            name='Test Variant Two',
            product=product
        )

        # Add variant_one to bag
        url = reverse('product_to_bag', kwargs={'product_id': product.id})
        current_page = f'/products/{product.id}/{variant_one.id}'
        post_data = {
            'current_page': current_page, 'product_variant': variant_one.id
        }
        self.client.post(url, data=post_data)

        # Check if variant_one they are in the bag and correctly formated
        product_bag_dict = {
            f'{product.id}': {'product_by_variant': {f'{variant_one.id}': 1}}
        }
        session = self.client.session
        self.assertEqual(session['bag'], product_bag_dict)

        # Add another variant_one so there should be 2
        self.client.post(url, data=post_data)

        # Check if there is 2 variant_one in bag
        product_bag_dict = {
            f'{product.id}': {'product_by_variant': {f'{variant_one.id}': 2}}
        }
        session = self.client.session
        self.assertEqual(session['bag'], product_bag_dict)

        # Add variant_two to bag
        url = reverse('product_to_bag', kwargs={'product_id': product.id})
        current_page = f'/products/{product.id}/{variant_two.id}'
        post_data = {
            'current_page': current_page, 'product_variant': variant_two.id
        }
        response = self.client.post(url, data=post_data)

        # Check if variant_two is add correctly to the same product
        product_bag_dict = {
            f'{product.id}': {
                'product_by_variant': {
                    f'{variant_one.id}': 2, f'{variant_two.id}': 1
                }
            }
        }
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
        product = Product.objects.create(
            name='Test Product',
            sizes=True, price='10',
            rating='0', rating_total='0',
            no_of_ratings='0'
        )

        # Add product to bag
        url = reverse('product_to_bag', kwargs={'product_id': product.id})
        current_page = f'/products/{product.id}'
        size_one = 'test_size_1'
        size_two = 'test_size_2'
        post_data = {'current_page': current_page, 'product_size': size_one}
        response = self.client.post(url, data=post_data)

        # Check if product with size in the bag and correctly formated
        product_bag_dict = {
            f'{product.id}': {'product_by_size': {f'{size_one}': 1}}
        }
        session = self.client.session
        self.assertEqual(session['bag'], product_bag_dict)

        # Add product with size_one again
        self.client.post(url, data=post_data)

        # Check if product with size_one quantity is 2
        product_bag_dict = {
            f'{product.id}': {'product_by_size': {f'{size_one}': 2}}
        }
        session = self.client.session
        self.assertEqual(session['bag'], product_bag_dict)

        # Add product with size_two
        url = reverse('product_to_bag', kwargs={'product_id': product.id})
        current_page = f'/products/{product.id}'
        post_data = {'current_page': current_page, 'product_size': size_two}
        self.client.post(url, data=post_data)

        # Check if product with size_one quantity is 2
        product_bag_dict = {
            f'{product.id}': {
                'product_by_size': {f'{size_one}': 2, f'{size_two}': 1}
            }
        }
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
        product = Product.objects.create(
            name='Test Product',
            price='10', rating='0',
            rating_total='0',
            no_of_ratings='0'
        )

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
        product = Product.objects.create(
            name='Test Product',
            price='10', rating='0',
            rating_total='0',
            no_of_ratings='0'
        )
        variant = Variant.objects.create(name='Test Variant', product=product)

        # Add product and its variant to bag
        url = reverse('product_to_bag', kwargs={'product_id': product.id})
        current_page = f'/products/{product.id}/{variant.id}'
        post_data = {
            'current_page': current_page, 'product_variant': variant.id
        }
        self.client.post(url, data=post_data)

        # Test quantity change
        quantity = random.randint(1, 10)
        post_data = {'quantity': quantity, 'product_variant': variant.id}
        url = reverse('update_bag', kwargs={'product_id': product.id})
        response = self.client.post(url, data=post_data)
        product_bag_dict = {
            f'{product.id}': {
                'product_by_variant': {f'{variant.id}': quantity}
            }
        }
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
        product = Product.objects.create(
            name='Test Product',
            sizes=True, price='10',
            rating='0', rating_total='0',
            no_of_ratings='0'
        )

        # Add product with size to bag
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
        product_bag_dict = {
            f'{product.id}': {'product_by_size': {f'{size}': quantity}}
        }
        session = self.client.session
        self.assertEqual(session['bag'], product_bag_dict)

        # Test Redirect
        self.assertRedirects(response, '/bag/')

    # Remove Product Only from Bag
    def test_remove_product_from_bag(self):
        """ Test the removal of a product from bag
        """

        # Create Product
        product = Product.objects.create(
            name='Test Product',
            price='10', rating='0',
            rating_total='0',
            no_of_ratings='0'
        )

        # Add product to bag
        url = reverse('product_to_bag', kwargs={'product_id': product.id})
        current_page = f'/products/{product.id}'
        post_data = {'current_page': current_page}
        self.client.post(url, data=post_data)

        # Check if product in the bag to be removed
        session = self.client.session
        self.assertEqual(session['bag'], {f'{product.id}': 1})

        # Remove Product
        url = reverse('remove_product', kwargs={'product_id': product.id})
        response = self.client.post(url)

        # Test product is removed
        session = self.client.session
        self.assertEqual(session['bag'], {})

        # Test Response of Removal
        self.assertEqual(response.status_code, 200)

    # Remove Product Variant from Bag
    def test_remove_product_with_variant_from_bag(self):
        """ Test the removal of a product with variant from bag
        """

        # Create Product & Vairant
        product = Product.objects.create(
            name='Test Product',
            price='10', rating='0',
            rating_total='0',
            no_of_ratings='0'
        )
        variant = Variant.objects.create(name='Test Variant', product=product)

        # Add them to bag
        url = reverse('product_to_bag', kwargs={'product_id': product.id})
        current_page = f'/products/{product.id}/{variant.id}'
        post_data = {
            'current_page': current_page, 'product_variant': variant.id
        }
        self.client.post(url, data=post_data)

        # Check if they are in the bag to be removed
        product_bag_dict = {
            f'{product.id}': {'product_by_variant': {f'{variant.id}': 1}}
        }
        session = self.client.session
        self.assertEqual(session['bag'], product_bag_dict)

        # Check if product and variant in the bag to be removed
        product_bag_dict = {
            f'{product.id}': {'product_by_variant': {f'{variant.id}': 1}}
        }
        session = self.client.session
        self.assertEqual(session['bag'], product_bag_dict)

        # Remove Product
        post_data = {'product_variant': variant.id}
        url = reverse('remove_product', kwargs={'product_id': product.id})
        response = self.client.post(url, data=post_data)

        # Test product is removed
        session = self.client.session
        self.assertEqual(session['bag'], {})

        # Test Response of Removal
        self.assertEqual(response.status_code, 200)

    # Remove Product with Size from Bag
    def test_remove_product_with_size_from_bag(self):
        """ Test the removal of a product with size from bag
        """

        # Create Product with Size
        product = Product.objects.create(
            name='Test Product',
            sizes=True, price='10',
            rating='0', rating_total='0',
            no_of_ratings='0'
        )

        # Add product to bag
        url = reverse('product_to_bag', kwargs={'product_id': product.id})
        current_page = f'/products/{product.id}'
        size = 'test_size'
        post_data = {'current_page': current_page, 'product_size': size}
        response = self.client.post(url, data=post_data)

        # Check if product with size in the bag to be removed
        product_bag_dict = {
            f'{product.id}': {'product_by_size': {f'{size}': 1}}
        }
        session = self.client.session
        self.assertEqual(session['bag'], product_bag_dict)

        # Remove Product
        post_data = {'product_size': size}
        url = reverse('remove_product', kwargs={'product_id': product.id})
        response = self.client.post(url, data=post_data)

        # Test product is removed
        session = self.client.session
        self.assertEqual(session['bag'], {})

        # Test Response of Removal
        self.assertEqual(response.status_code, 200)
