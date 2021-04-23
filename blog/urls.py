from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_blog, name='blog'),
    path(
        'delete_post/<int:post_id>/',
        views.delete_post,
        name='delete_post'
    ),
]
