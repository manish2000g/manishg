from django.test import TestCase

from django.test import TestCase
from django.test import TestCase
from.models import Category
class Category(TestCase):
   def setup(self):
       Category.objects.create(category_name="Goat")
   def test_grocery_type(self):
        qs=Category.objects.all()
        self.assertIsNotNone(qs)
   def test_on_save(self):
       print("testing the slug")
       product = Category()
       product.category_name = "Goat"
       product.save()
       self.assertEqual(product.category_name, "Goat")
   def test_home_page_code(self):
       print("testing the category page code")
       response = self.client.get('/categoriess/home/')
       self.assertEquals(response.status_code, 200)
       self.assertTemplateUsed(response, 'homepage.html')
