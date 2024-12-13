from . import views
from django.urls import path


app_name = "shop"
urlpatterns = [ 
      path('shop', views.Shop.as_view(), name='shop'),
      path('inventario', views.Inventario.as_view(), name='inventario'),
]