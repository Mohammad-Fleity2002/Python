from django.urls import path
from . import views
app_name = 'Password_Storage'
urlpatterns = [
    path('Add_Password/', views.Add_Password, name='Add_Password'),
    path('', views.index, name='index'),
]
