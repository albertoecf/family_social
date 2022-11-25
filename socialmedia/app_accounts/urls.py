from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
# we are using prebuild views -> auth_views
# and our views -> views


app_name = 'app_accounts'

urlpatterns = [
    path('login',
         auth_views.LoginView.as_view(template_name='app_accounts/login.html'),
         name='login'),
    path('logout',
         auth_views.LogoutView.as_view(),
         name='logout'),
    path('signup',
         views.SignUp.as_view(),
         name='signup')]
