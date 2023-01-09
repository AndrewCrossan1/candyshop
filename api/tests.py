from django.test import TestCase

from api.models import Category


# Shop Tests
class CategoryTests(TestCase):
    # Test Product Model
    def setUp(self):
        Category.objects.create(Name="Test Category",
                                Description="Test Description")

    def test_category_creation(self):
        # Test the product
        category = Category.objects.get(Name="Test Category")
        self.assertEqual(category.Name, "Test Category")

    def test_category_count(self):
        # Test the product count
        self.assertEqual(Category.objects.count(), 1)

    def test_category_deletion(self):
        # Delete the product
        category = Category.objects.get(Name="Test Category")
        category.delete()
        self.assertEqual(Category.objects.count(), 0)
