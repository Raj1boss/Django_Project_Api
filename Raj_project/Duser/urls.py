from django.urls import path
from . import views
urlpatterns = [
    path('', views.Signup, name='register'),
    path('slogin', views.Login, name='login'),
    path('opslogin', views.opsLogin, name='opslogin'),
    path('logout', views.Logout, name='logout'),
    path('ulogout', views.uLogout, name='ulogout'),
    path('home', views.home, name='home'),
    path('dashboard', views.dashboard, name='dashboard'),
]
