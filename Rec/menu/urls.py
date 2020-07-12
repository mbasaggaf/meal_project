
from django.urls import path, include
from . import views
app_name = 'menu'
urlpatterns = [
    path('', views.home, name='home'),
    path('companys/', views.allcompany, name="allcompany"),
    path('newcompany/', views.newcompany, name = 'newcompany'),
    path('company/<pk>/',views.companydetul, name='companydetul'),


]
