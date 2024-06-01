from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_api_response, name='get_api_response'),
]