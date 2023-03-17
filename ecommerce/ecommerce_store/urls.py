from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter
from rest_framework.urlpatterns import format_suffix_patterns

from ecommerce_store.views import user_view, ecommerce_store_view

urlpatterns = [
    path('users/', user_view.EcommerceUserAPIView.as_view(), name='users-list'),
    path('users/<int:pk>', user_view.EcommerceUserDetailAPIView.as_view(), name='users-detail'),
    path('ecommerces/', ecommerce_store_view.EcommerceStoreApiView.as_view(), name='ecommerce-list'),
    path('ecommerces/<int:pk>', ecommerce_store_view.EcommerceStoreDetailApiView.as_view(), name='ecommerce-detail')
]
