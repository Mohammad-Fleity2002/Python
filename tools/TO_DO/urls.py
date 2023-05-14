from django.urls import path
from . import views
app_name = 'TO_DO'
urlpatterns = [
    path('', views.index, name='index'),
    path('deletTask/<int:item_id>', views.deletTask, name='deletTask'),
    path('all_task/deletTask/<int:item_id>',
         views.deletTask, name='deletTask'),
    path('checkTask/<int:item_id>', views.checkTask, name='checkTask'),
    path('all_task/', views.allTask, name="allTask"),
]
