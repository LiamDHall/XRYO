from django.test import TestCase
from . models import Product, Variant

# Create your tests here.


class TestProductViews(TestCase):

    def test_all_products(self):
        """ Tests response and if template is correct
        """

        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_product_detail(self):
        """ Creates test product (without variant) and checks if the
        correct template rendered to display the product details
        """

        product = Product.objects.create(name='Test Product')
        response = self.client.get(f'/products/{product.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_detail.html')

    def test_product_variant(self):
        """ Creates test product with variant and checks if the
        correct template rendered to display the variant's details
        """

        product = Product.objects.create(name='Test Product')
        variant = Variant.objects.create(name='Test Variant', product=product)
        response = self.client.get(f'/products/{product.id}/{variant.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_variant.html')
