from django.urls import path

from . import views
app_name = 'Authentications'
urlpatterns = [
    path('', views.login_user, name="login"),
    path('logout_user/', views.logout_user, name="logout"),
    path('sign_up', views.sign_up, name="sign_up"),
]
