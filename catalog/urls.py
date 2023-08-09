from django.urls import path

from catalog.apps import CatalogConfig
from . import views


app_name = CatalogConfig.name

urlpatterns = [
    path('', views.ProductListView.as_view()),
    path('contacts/', views.ProductContactView.as_view()),
    path('product/<int:pk>/', views.ProductDetailView.as_view(), name='product_card')
]
