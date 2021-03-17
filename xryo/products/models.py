from django.db import models
from django.db.models import signals


def get_upload_path(instance, filename):
    """Creates the upload path for the image based off the album
    selected, with Pillow installed the file directory will be created
    (if not already) in the media folder and the file will be uploaded.
    """

    model = instance.album.model.__class__._meta
    album = instance.album.model.name
    name = model.verbose_name_plural.lower().replace(' ', '_')
    return f'{name}/{album}/{filename}'


def create_image_album(sender, instance, created, **kwargs):
    """Create ImageAlbum for every new Product
    """

    name = instance.name
    if created:
        ImageAlbum.objects.create(name=name)
        album = ImageAlbum.objects.get(name=name)
        instance.album = album
        instance.save()


class ImageAlbum(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

    def default(self):
        return self.images.filter(default=True).first()


class Image(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to=get_upload_path)
    default = models.BooleanField(default=False)
    album = models.ForeignKey(
        ImageAlbum,
        related_name='images',
        null=True, blank=True,
        on_delete=models.SET_NULL
    )


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
    description = models.TextField(blank=True)
    rating = models.DecimalField(max_digits=6, decimal_places=1, default=0.00)
    rating_total = models.IntegerField(default=0)
    no_of_ratings = models.IntegerField(default=0)
    album = models.OneToOneField(
        ImageAlbum,
        related_name='model',
        null=True, blank=True,
        on_delete=models.SET_NULL
    )

    def __str__(self):
        return self.name


""" Signal to trigger the auto creation of the ImageAlbum,
must be below Product class
"""

signals.post_save.connect(create_image_album, sender=Product, weak=False,
                          dispatch_uid='models.create_image_album')


class Variant(models.Model):
    product = models.ForeignKey(
        'Product', null=True, blank=True, on_delete=models.SET_NULL
    )
    price = models.DecimalField(max_digits=6, decimal_places=2)
    sku = models.CharField(max_length=100, null=True, blank=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
