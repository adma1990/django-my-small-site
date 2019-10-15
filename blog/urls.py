from django.urls import path

from .views import *

urlpatterns = [
   path('', index, name = "index"),
   path('product/<str:slug>/', product, name = "product"),
   path('katalog/', katalog, name = "katalog"),
   path('contacts/', contacts, name = "contacts"),
   path('form/', form, name = "form"),
   path('delivery/', delivery, name= "delivery"),

]
