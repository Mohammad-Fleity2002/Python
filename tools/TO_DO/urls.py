from django.urls import path
from . import views
app_name = 'TO_DO'
urlpatterns = [
    path('', views.index, name='index'),
]
