from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_bag, name='view_bag'),
    path('add/<product_id>/', views.product_to_bag, name='product_to_bag'),
    path('update/<product_id>/', views.update_bag, name='update_bag'),
    path('remove/<product_id>/', views.remove_product, name='remove_product'),
]
