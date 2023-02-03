from django.urls import path
from .views import home, pasword


app_name = "generator"

urlpatterns = [
    path('', home, name='index'),
    path('password/', pasword, name='pasword'),
]