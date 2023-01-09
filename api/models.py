from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from taggit.managers import TaggableManager


# Shop Models here
class Category(models.Model):
    CategoryID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=120)
    Description = models.TextField()
    Tags = TaggableManager()

    @property
    def product_count(self):
        return self.product_set.count()

    @property
    def average_rating(self):
        total = 0
        for product in self.product_set.all():
            total += product.Rating
        return total / self.product_set.count()

    class Meta:
        verbose_name_plural = "Categories"
        verbose_name = "Category"
        ordering = ['Name']

    def __str__(self):
        return self.Name


class Brand(models.Model):
    BrandID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=120)
    Description = models.TextField()
    Tags = TaggableManager()

    @property
    def product_count(self):
        return self.product_set.count()

    class Meta:
        verbose_name_plural = "Brands"
        verbose_name = "Brand"
        ordering = ['Name']

    def __str__(self):
        return self.Name


class Product(models.Model):
    ProductID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=120)
    Description = models.TextField()
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    Image = models.ImageField(upload_to='images/', blank=True, null=True)
    Category = models.ForeignKey('Category', on_delete=models.CASCADE)
    Tags = TaggableManager()
    Rating = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    Brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    Stock = models.IntegerField(default=0)
    Available = models.BooleanField(default=True)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)

    @property
    def category_name(self):
        return self.Category.Name

    @property
    def brand_name(self):
        return self.Brand.Name

    @staticmethod
    def top_rated_products():
        return Product.objects.order_by('-Rating')[:5]

    class Meta:
        verbose_name_plural = "Products"
        verbose_name = "Product"
        ordering = ['Name']

    def __str__(self):
        return self.Name
