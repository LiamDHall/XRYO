from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<product_id>', views.product_detail, name='product_detail'),
    path('<product_id>/<variant_id>', views.product_variant, name='product_variant'),
]