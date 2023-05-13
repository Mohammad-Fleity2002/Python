from django.urls import path
from . import views
app_name = 'Password_Storage'
urlpatterns = [
    path('Add_Password/', views.AddPassword, name='AddPassword'),
    path('', views.index, name='index'),
]
