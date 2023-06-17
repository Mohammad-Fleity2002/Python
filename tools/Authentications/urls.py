from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
app_name = 'Authentications'
urlpatterns = [
    path('', views.login_user, name="login"),
    path('logout_user/', views.logout_user, name="logout"),
    path('sign_up/', views.sign_up, name="sign_up"),
    path('change_password/', views.change_pass, name="change_pass"),
    # path('change_password/', auth_views.PasswordChangeView.as_view(
    #     template_name="Registration/change_password.html")),

]
