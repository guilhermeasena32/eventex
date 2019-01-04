from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Guilherme Sena', cpf='12345678901',
                    email='guilherme@sena.com', phone='31-99238-7080')
        self.resp = self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de incrição'

        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@eventex.com.br'

        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@eventex.com.br', 'guilherme@sena.com']

        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = [
            'Guilherme Sena',
            '12345678901',
            'guilherme@sena.com',
            '31-99238-7080',
        ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
