from django.test import TestCase

from api.models import Category, Brand, Product


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


class BrandTests(TestCase):
    # Test Product Model
    def setUp(self):
        Brand.objects.create(Name="Test Brand",
                             Description="Test Description")

    def test_brand_creation(self):
        # Test the product
        brand = Brand.objects.get(Name="Test Brand")
        self.assertEqual(brand.Name, "Test Brand")

    def test_brand_count(self):
        # Test the product count
        self.assertEqual(Brand.objects.count(), 1)

    def test_brand_deletion(self):
        # Delete the product
        brand = Brand.objects.get(Name="Test Brand")
        brand.delete()
        self.assertEqual(Brand.objects.count(), 0)


class ProductTest(TestCase):
    # Test Product Model
    def setUp(self):
        category = Category.objects.create(
            Name="Test Category",
            Description="Test Description")
        brand = Brand.objects.create(
            Name="Test Brand",
            Description="Test Description")
        Product.objects.create(
            Name="Test Product",
            Description="Test Description",
            Category=category,
            Brand=brand,
            Price=100,
            Stock=10,
            Image="test.jpg")

    def test_product_creation(self):
        # Test the product
        product = Product.objects.get(Name="Test Product")
        self.assertEqual(product.Name, "Test Product")

    def test_product_count(self):
        # Test the product count
        self.assertEqual(Product.objects.count(), 1)

    def test_product_deletion(self):
        # Delete the product
        product = Product.objects.get(Name="Test Product")
        product.delete()
        self.assertEqual(Product.objects.count(), 0)

    def test_product_update(self):
        # Update the product
        product = Product.objects.get(Name="Test Product")
        product.Name = "Updated Product"
        product.save()
        self.assertEqual(Product.objects.get(Name="Updated Product").Name,
                         "Updated Product")

    def test_product_category_update(self):
        # Update the product
        product = Product.objects.get(Name="Test Product")
        category = Category.objects.create(Name="Test Category 2",
                                           Description="Test Description")
        product.Category = category
        product.save()
        self.assertEqual(Product.objects.get(Name="Test Product").Category,
                         category)

    def test_product_brand_update(self):
        # Update the product
        product = Product.objects.get(Name="Test Product")
        brand = Brand.objects.create(Name="Test Brand 2",
                                     Description="Test Description")
        product.Brand = brand
        product.save()
        self.assertEqual(Product.objects.get(Name="Test Product").Brand,
                         brand)

    def test_product_price_update(self):
        # Update the product
        product = Product.objects.get(Name="Test Product")
        product.Price = 200
        product.save()
        self.assertEqual(Product.objects.get(Name="Test Product").Price,
                         200)

    def test_product_quantity_update(self):
        # Update the product
        product = Product.objects.get(Name="Test Product")
        product.Stock = 20
        product.save()
        self.assertEqual(Product.objects.get(Name="Test Product").Stock,
                         20)
