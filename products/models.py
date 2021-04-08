from django.db import models
from django.db.models import signals
from django.conf import settings

from PIL import Image

ImageTool = Image
media_url = settings.MEDIA_URL.lstrip("/")


def get_upload_path(instance, filename):
    """Creates the upload path for the image,
    with Pillow installed the file directory will be created
    (if not already) in the media folder and the file will be uploaded.
    """
    ablum_name = instance.album.name.lower()
    return f'product_images/{ablum_name}/{filename}'


def create_or_upadate_image_album(sender, instance, created, **kwargs):
    """Create ImageAlbum for every new Product or Variant.
    ImageAlbum is a Joining Table. If the name of the Product or
    Variant change this function will update the album name to match
    it.
    """

    name = instance.name
    if created:
        if not ImageAlbum.objects.filter(name=name).exists():
            ImageAlbum.objects.create(name=name)
        album = ImageAlbum.objects.get(name=name)
        instance.album = album
        instance.save()

    elif instance.album and instance.name != instance.album.name:
        album_id = instance.album.id
        album = ImageAlbum.objects.get(pk=album_id)
        album.name = name
        album.save()


class ImageAlbum(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

    def default(self):
        return self.images.filter(default=True).first()


def resize_image(sender, instance, created, **kwargs):
    """Resize images so if sligtly different they will
    all be uniform
    """

    if created:
        image = ImageTool.open(f'{media_url}{instance.image}')
        image = image.resize((1600, 2000))
        image.save(f'{media_url}{instance.image}')


class Image(models.Model):
    name = models.CharField(max_length=255)
    default = models.BooleanField(default=False)
    album = models.ForeignKey(
        ImageAlbum,
        related_name='images',
        null=True, blank=True,
        on_delete=models.SET_NULL
    )

    image = models.ImageField(upload_to=get_upload_path)

    def __str__(self):
        return self.name


""" Signal to trigger the resizing of Images.

MUST BE BELOW IMAGE CLASS AND FUNCTION IT CALLS
"""

signals.post_save.connect(
    resize_image,
    sender=Image,
    weak=False,
    dispatch_uid='models.create_image'
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
    class_name = 'product'
    name = models.CharField(max_length=100)
    price = models.DecimalField(
        max_digits=6, decimal_places=2, default=900
    )
    sizes = models.BooleanField(default=False, null=True, blank=True)
    sku = models.CharField(max_length=100, null=True, blank=True)
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


""" Signal to trigger the auto creation of the ImageAlbum, or update
name of album to match product name.

MUST BE BELOW PRODUCT CLASS AND FUNCTION IT CALLS
"""

signals.post_save.connect(
    create_or_upadate_image_album,
    sender=Product,
    weak=False,
    dispatch_uid='models.create_image_album'
)


class Variant(models.Model):
    product = models.ForeignKey(
        'Product', on_delete=models.CASCADE
    )
    class_name = 'variant'
    sku = models.CharField(max_length=100, null=True, blank=True)
    name = models.CharField(max_length=100)
    album = models.OneToOneField(
        ImageAlbum,
        related_name='variant_model',
        null=True, blank=True,
        on_delete=models.SET_NULL
    )

    def __str__(self):
        return self.name


""" Signal to trigger the auto creation of the ImageAlbum, or update
name of album to match product name.

MUST BE BELOW VARIANT CLASS AND FUNCTION IT CALLS
"""

signals.post_save.connect(
    create_or_upadate_image_album,
    sender=Variant,
    weak=False,
    dispatch_uid='models.create_image_album'
)
