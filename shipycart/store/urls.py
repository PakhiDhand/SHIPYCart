from django.contrib import admin
from django.urls import path
from store.views import store_home, product_detail, search

urlpatterns = [ 
    path("", store_home, name="shipy-store-home"),
    path('search/', search, name='search'),
    path("<slug:category_slug>/", store_home, name="shipy-store-category"),
    path("<slug:category_slug>/<slug:product_slug>", product_detail, name="shipy-product-detail"),
]
