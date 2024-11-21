from . import views
from django.urls import path


app_name = "mensapp"
urlpatterns = [ 
      path('mensapp', views.MensApp.as_view(), name='mensapp'),

]