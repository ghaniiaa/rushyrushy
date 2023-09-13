from django.test import TestCase, Client

class mainTest(TestCase):
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

