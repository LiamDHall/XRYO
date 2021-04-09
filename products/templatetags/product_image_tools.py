from django import template
from django.shortcuts import get_object_or_404

from ..models import ImageAlbum, Image


register = template.Library()


@register.filter(name='get_thumbnail')
def get_thumbnail(album_id):
    """Gets the defualt image from the album.
    If no default image the first image will be set instead.
    """
    album = get_object_or_404(ImageAlbum, pk=album_id)
    defualt_images = Image.objects.all().filter(album=album, default=True)
    defualt_list = list(defualt_images)
    if len(defualt_list) > 0:
        defualt_image = defualt_images.get()
        return defualt_image.image
    else:
        first_image = Image.objects.all().filter(album=album).first()
        return first_image.image
