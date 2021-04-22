from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver

from .models import Product, Image, Variant, Review


@receiver(post_save, sender=Product)
def set_or_update_product_image_album(sender, instance, created, **kwargs):
    """ Creates or renames product album on product save.
    """
    instance.create_or_upadate_image_album(created)


@receiver(pre_delete, sender=Product)
def delete_product_album_on_delete(sender, instance, **kwargs):
    """ Delete ablum on product deletion
    """
    instance.delete_image_album()


@receiver(post_save, sender=Variant)
def set_or_update_variant_image_album(sender, instance, created, **kwargs):
    """ Creates or renames variant album on product save.
    """
    instance.create_or_upadate_image_album(created)


@receiver(pre_delete, sender=Variant)
def delete_variant_album_on_delete(sender, instance, **kwargs):
    """ Delete ablum on variant deletion
    """
    instance.delete_image_album()


@receiver(post_save, sender=Image)
def resize_image_on_image_creation(sender, instance, created, **kwargs):
    """ Resize image when image is created
    """
    instance.resize_image(created)


@receiver(post_save, sender=Review)
def update_product_rating_on_review_save(sender, instance, **kwargs):
    """ Update product rating on review submission
    """
    instance.update_product_rating()
