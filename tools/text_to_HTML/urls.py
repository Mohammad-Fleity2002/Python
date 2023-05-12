from django.urls import path
from . import views
app_name = 'text_to_HTML'
urlpatterns = [
    path('', views.index, name='index'),
]
