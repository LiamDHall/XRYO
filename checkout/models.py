import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings

from django_countries.fields import CountryField

from products.models import Product, Variant
from profiles.models import Profile


class Order(models.Model):
    user_profile = models.ForeignKey(
        Profile,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='orders'
    )
    order_number = models.CharField(
        max_length=32,
        null=False,
        editable=False
    )
    date = models.DateTimeField(auto_now_add=True)
    full_name = models.CharField(
        max_length=50,
        null=False,
        blank=False
    )
    email = models.EmailField(
        max_length=254,
        null=False,
        blank=False
    )
    phone_number = models.CharField(
        max_length=20,
        null=False,
        blank=False
    )
    street_address1 = models.CharField(
        max_length=80,
        null=False,
        blank=False
    )
    street_address2 = models.CharField(
        max_length=80,
        null=True,
        blank=True
    )
    town_or_city = models.CharField(
        max_length=40,
        null=False,
        blank=False
    )
    county = models.CharField(
        max_length=80,
        null=True,
        blank=True
    )
    postcode = models.CharField(
        max_length=20,
        null=True,
        blank=True
    )
    country = CountryField(
        blank_label="Country *",
        null=False,
        blank=False
    )
    delivery_charge = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=False,
        default=0
    )
    order_total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=False,
        default=0
    )
    grand_total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=False,
        default=0
    )
    original_bag = models.TextField(
        null=False,
        blank=False,
        default=''
    )
    stripe_pid = models.CharField(
        max_length=254,
        null=False,
        blank=False,
        default=''
    )

    def _create_order_number(self):
        """ Create a random unique order number
        """

        return uuid.uuid4().hex.upper()

    def update_total(self):
        """ Update grand total when an item is added taking into
        account delivery charge.
        """

        self.order_total = self.items.aggregate(Sum('item_total'))['item_total__sum'] or 0
        if self.order_total < settings.FREE_DELIVERY_MIN:
            self.delivery_charge = settings.DELIVERY_CHARGE
        else:
            self.delivery_charge = 0

        self.grand_total = self.order_total + self.delivery_charge
        self.save()

    def save(self, *args, **kwargs):
        """Replace the original save method to add addition function.
        Sets the order number if not already set.
        """

        if not self.order_number:
            self.order_number = self._create_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name='items'
    )
    product = models.ForeignKey(
        Product,
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )
    variant = models.ForeignKey(
        Variant,
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )
    product_size = models.CharField(
        max_length=3,
        null=True,
        blank=True
    )
    quantity = models.IntegerField(
        null=False,
        blank=False,
        default=0
    )
    item_total = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=False,
        blank=False,
        editable=False
    )

    def save(self, *args, **kwargs):
        """ Replace the original save method to add addition function.
        Sets the item total and update the order total.
        """

        self.item_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'SKU {self.product.sku} on order {self.order.order_number}'
