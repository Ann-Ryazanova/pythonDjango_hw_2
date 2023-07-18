from django.urls import path

from catalog.apps import CatalogConfig
from . import views

# from catalog.views import home, contacts, product_card

app_name = CatalogConfig.name

urlpatterns = [
    path('', views.home),
    path('contacts/', views.contacts),
    path('product/<int:pk>/', views.ProductDetailView.as_view(), name='product_card')

    # <img src="/{{ BASIC_DIR }}/{{media.media}} class="card-img-top">
]
