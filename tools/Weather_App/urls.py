from django.urls import path
from . import views
app_name = 'Weather'

urlpatterns = [
    path('', views.index, name="index"),
]
