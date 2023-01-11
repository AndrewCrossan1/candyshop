from django.contrib import admin
from django.db import models
from django.utils.html import format_html
from taggit.managers import TaggableManager
from users.models import User


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
        if self.product_set.count() == 0:
            return 0
        total = 0
        for product in self.product_set.all():
            total += product.Prop_Rating
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
    Brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    Stock = models.IntegerField(default=0)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)

    @property
    def category_name(self):
        return self.Category.Name

    @property
    def Prop_Rating(self):
        Total = 0
        if self.productrating_set.count() == 0:
            return 0
        for rating in self.productrating_set.all():
            Total += rating.Rating
        return Total / self.productrating_set.count()

    @property
    def Available(self):
        return self.Stock > 0

    @property
    def brand_name(self):
        return self.Brand.Name

    def Highest_Rated(self):
        queryset = self.Category.product_set.all()
        if queryset.count() == 0:
            return False
        Max = queryset[0]
        for item in queryset[1:]:
            if item.Prop_Rating > Max.Prop_Rating:
                Max = item
        return self == Max

    def below_average(self):
        return self.Prop_Rating < self.Category.average_rating

    @admin.display
    def Availability(self):
        if self.Available:
            return format_html(
                '<span style="font-weight: bold; color: green;">{}</span>',
                self.Available
            )
        else:
            return format_html(
                '<span style="font-weight: bold; color: red;">{}</span>',
                self.Available
            )

    @admin.display
    def Rating(self):
        if self.Highest_Rated():
            return format_html(
                '<span style="color: gold; font-weight: bold;">{}</span>',
                self.Prop_Rating
            )
        elif self.below_average() is True:
            return format_html(
                '<span style="color: red; font-weight: bold;">{}</span>',
                self.Prop_Rating
            )
        else:
            return format_html(
                '<span style="color: green; font-weight: bold;">{}</span>',
                self.Prop_Rating
            )

    @staticmethod
    def top_rated_products():
        return Product.objects.order_by('-Prop_Rating')[:5]

    class Meta:
        verbose_name_plural = "Products"
        verbose_name = "Product"
        ordering = ['Name']

    def __str__(self):
        return self.Name

    def __unicode__(self):
        return self.Category.Name


class ProductRating(models.Model):
    RATING_CHOICES = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5)
    ]
    RatingID = models.AutoField(primary_key=True)
    Product = models.ForeignKey(Product, on_delete=models.CASCADE)
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Rating = models.IntegerField(choices=RATING_CHOICES)
    Date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['RatingID']
        verbose_name = 'Product Rating'
        verbose_name_plural = 'Product Ratings'

    def __str__(self):
        return f'Rating by {self.User.email}'
