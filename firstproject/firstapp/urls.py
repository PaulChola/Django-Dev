from django.urls import path 
from . import views


urlpatterns = [
 path('functions', views.hello_world),
 path('class', views.HelloEthiopia.as_view()),
 path('reservation', views.home),
]
