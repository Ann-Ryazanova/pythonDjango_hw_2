from django.urls import path

from catalog.apps import CatalogConfig
from . import views


app_name = CatalogConfig.name

urlpatterns = [
    path('create/', views.ProductCreateView.as_view(), name='create_product'),
    path('', views.ProductListView.as_view(), name='list'),
    path('contact/', views.ProductContactView.as_view()),
    path('product/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('edit/<int:pk>/', views.ProductUpdateView.as_view(), name='update_product'),
    path('delete/<int:pk>/', views.ProductDeleteView.as_view(), name='delete_product'),
]
