from django.urls import path
from . import views
app_name = 'My_Contact'
urlpatterns = [
    path('Add_Contact/', views.AddContact, name='AddContact'),
    path('deleteContact/<int:item_id>',views.deleteContact, name='deleteContact'),
    path('', views.index, name='index'),
]
