from django.db import models
from django.contrib.postgres.fields import ArrayField


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=100)
    display_name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_display_name(self):
        return self.display_name


class Product(models.Model):
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL
    )
    name = models.CharField(max_length=100)
    description = models.TextField()
    rating = models.DecimalField(max_digits=6, decimal_places=1, default=0.00)
    rating_total = models.IntegerField(default=0)
    no_of_ratings = models.IntegerField(default=0)
    images = ArrayField(models.ImageField(null=True, blank=True), default=list)

    def __str__(self):
        return self.name


class Variant(models.Model):
    product = models.ForeignKey(
        'Product', null=True, blank=True, on_delete=models.SET_NULL
    )
    price = models.DecimalField(max_digits=6, decimal_places=2)
    sku = models.CharField(max_length=100, null=True, blank=True)
    name = models.CharField(max_length=100)
    images = ArrayField(models.ImageField(null=True, blank=True), default=list)

    def __str__(self):
        return self.name
