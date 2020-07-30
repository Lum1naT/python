from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('userdetail/<int:user_id>/', views.user_detail, name='detail'),
    path('register/', views.register_user, name='register user'),
    path('email_test/', views.email_test, name='email test'),

]
