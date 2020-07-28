from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('register/', views.register, name='register'),
    path('login/', views.log, name='login'),
    path('test/', views.test, name='test'),
    path('logout/', views.lout, name='logout'),
]
