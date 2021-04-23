from django.db import models


class Post(models.Model):
    title = models.CharField(
        max_length=52,
        null=False,
        blank=False
    )

    date = models.DateTimeField(auto_now_add=True)

    article = models.CharField(
        max_length=450,
        null=False,
        blank=False
    )

    image = models.ImageField(upload_to='blog_images/')

    def __str__(self):
        return self.title
