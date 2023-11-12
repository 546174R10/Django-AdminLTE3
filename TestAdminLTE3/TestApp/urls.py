from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


app_name = 'TestApp'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),

 ]