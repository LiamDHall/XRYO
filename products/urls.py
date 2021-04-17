from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path(
        '<int:product_id>/<variant_id>/',
        views.product_variant,
        name='product_variant'
    ),
    path('add/', views.add_product, name='add_product'),
]
