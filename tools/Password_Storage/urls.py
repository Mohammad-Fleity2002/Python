from django.urls import path
from . import views
app_name = 'Password_Storage'
urlpatterns = [
    path('Add_Password/', views.AddPassword, name='AddPassword'),
    # path('<int:pass_id>', views.editPassword, name='editPassword'),
    path('deletePassword/<int:item_id>',
         views.deletePassword, name='deletePassword'),
    path('', views.index, name='index'),

]
