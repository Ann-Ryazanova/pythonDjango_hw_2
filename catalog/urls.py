from django.urls import path
from django.views.decorators.cache import cache_page, never_cache

from catalog.apps import CatalogConfig
from . import views

app_name = CatalogConfig.name

urlpatterns = [
    path('create/', never_cache(views.ProductCreateView.as_view()), name='create_product'),
    path('', views.ProductListView.as_view(), name='list'),
    path('contact/', views.ProductContactView.as_view(), name='contacts'),
    path('product/<int:pk>/', cache_page(60)(views.ProductDetailView.as_view()), name='product_detail'),
    path('edit/<int:pk>/', never_cache(views.ProductUpdateView.as_view()), name='update_product'),
    path('delete/<int:pk>/', views.ProductDeleteView.as_view(), name='delete_product'),
]
