from django.test import TestCase
from Project.Classes.Account import Account

class AccountTestCase(TestCase):
    def setUp(self):
        Animal.objects.create(name="lion", sound="roar")
        Animal.objects.create(name="cat", sound="meow")

