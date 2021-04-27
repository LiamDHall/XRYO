from django.db import models
from django.conf import settings

from decimal import Decimal

from .feilds import IntegerRangeField

from PIL import Image as ImageTool

media_url = settings.MEDIA_URL.lstrip("/")


def get_upload_path(instance, filename):
    """Creates the upload path for the image,
    with Pillow installed the file directory will be created
    (if not already) in the media folder and the file will be uploaded.
    """
    if instance.album.name.lower():
        album_name = instance.album.name.lower()
        return f'product_images/{album_name}/{filename}'
    else:
        return f'product_images/{filename}'


class ImageAlbum(models.Model):
    """ Joining Table
    Allow many to many relationship between Variant or Product and
    images.
    """
    name = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.name


class Image(models.Model):
    name = models.CharField(max_length=200)
    default = models.BooleanField(default=False)
    album = models.ForeignKey(
        ImageAlbum,
        related_name='images',
        null=True, blank=True,
        on_delete=models.CASCADE,
    )

    image = models.ImageField(upload_to=get_upload_path)

    def resize_image(self, created):
        """Resize images so if sligtly different they will
        all be uniform
        """

        if created:
            image = ImageTool.open(f'{media_url}{self.image}')
            image = image.resize((1600, 2000))
            image.save(f'{media_url}{self.image}')

    def set_default(self):
        """Set default the sender image as default of
        album and remove default from the current
        default image
        """

        album = self.album
        default_images = Image.objects.all().filter(
            album=album, default=True
        )

        if len(default_images) > 1 and self.default is True:
            for image in default_images:
                image.default = False
                image.save()

            self.default = True
            self.save()

    def __str__(self):
        return self.name


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=50)
    display_name = models.CharField(max_length=75, null=True, blank=True)

    def get_display_name(self):
        return self.display_name

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL
    )
    class_name = 'product'
    name = models.CharField(max_length=50)
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
    )
    sizes = models.BooleanField(default=False, null=True, blank=True)
    sku = models.CharField(max_length=25, null=True, blank=True)
    description = models.TextField(blank=True)
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=0.0)
    rating_total = models.PositiveIntegerField(default=0)
    no_of_ratings = models.PositiveIntegerField(default=0)
    album = models.OneToOneField(
        ImageAlbum,
        related_name='model',
        null=True, blank=True,
        on_delete=models.SET_NULL
    )

    def create_or_upadate_image_album(self, created):
        """Create ImageAlbum for every new Product or Variant.
        ImageAlbum is a Joining Table. If the name of the Product or
        Variant change this function will update the album name to match
        it.
        """

        sender_name = self.name.lower().replace(" ", "_")
        sender_id = self.id
        album_name = f'{sender_name}_id_{sender_id}'
        if created:
            if not ImageAlbum.objects.filter(name=album_name).exists():
                ImageAlbum.objects.create(name=album_name)
            album = ImageAlbum.objects.get(name=album_name)
            self.album = album
            self.save()

        elif self.album and self.name != self.album.name:
            album_id = self.album.id
            album = ImageAlbum.objects.get(pk=album_id)
            album.name = album_name
            album.save()

    def delete_image_album(self):
        """Delete the image album of the product
        """
        if self.album:
            self.album.delete()

    def __str__(self):
        return self.name


class Variant(models.Model):
    product = models.ForeignKey(
        'Product', on_delete=models.CASCADE
    )
    class_name = 'variant'
    sku = models.CharField(max_length=25, null=True, blank=True)
    name = models.CharField(
        max_length=50,
        null=False,
        blank=False,
    )
    album = models.OneToOneField(
        ImageAlbum,
        related_name='variant_model',
        null=True, blank=True,
        on_delete=models.SET_NULL
    )

    def create_or_upadate_image_album(self, created):
        """Create ImageAlbum for every new Product or Variant.
        ImageAlbum is a Joining Table. If the name of the Product or
        Variant change this function will update the album name to match
        it.
        """

        sender_name = self.name.lower().replace(" ", "_")
        sender_id = self.id
        album_name = f'{sender_name}_id_{sender_id}'
        if created:
            if not ImageAlbum.objects.filter(name=album_name).exists():
                ImageAlbum.objects.create(name=album_name)
            album = ImageAlbum.objects.get(name=album_name)
            self.album = album
            self.save()

        elif self.album and self.name != self.album.name:
            album_id = self.album.id
            album = ImageAlbum.objects.get(pk=album_id)
            album.name = album_name
            album.save()

    def delete_image_album(self):
        """Delete the image album of the product
        """
        if self.album:
            self.album.delete()

    def __str__(self):
        return self.name


class Review(models.Model):
    product = models.ForeignKey(
        'Product',
        on_delete=models.CASCADE,
    )
    date = models.DateTimeField(auto_now_add=True)
    user_name = models.CharField(
        max_length=25,
        null=False,
        blank=False,
        default='Anonymous'
    )
    rating = IntegerRangeField(min_value=1, max_value=5)
    comment = models.CharField(max_length=400, null=True, blank=True)

    def update_product_rating(self):
        self.product.no_of_ratings += 1
        self.product.rating_total += self.rating

        no_of_ratings = self.product.no_of_ratings
        rating_total = self.product.rating_total

        new_rating = rating_total / no_of_ratings

        self.product.rating = Decimal(round(new_rating, 1))

        self.product.save()

    def __str__(self):
        return f'{self.user_name} {self.product.name} Review'
