from django.test import TestCase


class HomeTest(TestCase):
    def setUp(self):
        self.response = self.client.get('/')

    def test_get(self):
        """GET / must return status code 200"""
        self.assertEqual(200, self.response.status_code)
        # essa funcao testa se o status code retornado é igual a 200

    def test_template(self):
        """Must use index.html"""
        self.assertTemplateUsed(self.response, 'index.html')
        # essa funcao testa se o template usado na home é o index.html

    def test_subscription_link(self):
        self.assertContains(self.response, 'href="/inscricao/"')
        # essa funcao testa se tem href inscricao na home(index.html)
