from django.test import TestCase, Client
from .models import Product

class MainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main.html')

    def test_main_contains_name(self):
        response = Client().get('/main/')
        self.assertContains(response, 'Ghania Larasati Nurjayadi Putri')

    def test_main_contains_class(self):
        response = Client().get('/main/')
        self.assertContains(response, 'PBP D')

    def test_main_template_context(self):
        response = Client().get('/main/')
        self.assertEqual(response.context['name'], 'Ghania Larasati Nurjayadi Putri')
        self.assertEqual(response.context['class'], 'PBP D')

class ProductTestCase(TestCase):
    def setUp(self):
        self.product = Product.objects.create(
            name='Test Product',
            amount=10,
            description='This is a test product',
            category='Test Category',
            price=100
        )

    def test_product_creation(self):
        product = Product.objects.get(name='Test Product')
        self.assertEqual(product.amount, 10)
        self.assertEqual(product.description, 'This is a test product')
        self.assertEqual(product.category, 'Test Category')
        self.assertEqual(product.price, 100)

    def test_product_string_representation(self):
        self.assertEqual(str(self.product), 'Test Product')

    def test_product_date_added_auto_now_add(self):
        self.assertIsNotNone(self.product.date_added)
