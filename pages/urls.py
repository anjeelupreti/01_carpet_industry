from django.contrib import admin
from django.urls import path, include
from .views import homepage, contact_us, about_us, products,product_detail, gallery, manufacturing, history

urlpatterns = [
    path('', homepage , name='homepage'),
    path('contact-us/', contact_us , name='contact_us'),
    path('about-us/', about_us , name='about_us'),
    path('products/', products , name='products'),
    path('product_detail/', product_detail , name='product_detail'),
    path('gallery/', gallery , name='gallery'),
    path('manufacturing-process/', manufacturing , name='manufacturing'),
    path('history/', history , name='history'),


   
]