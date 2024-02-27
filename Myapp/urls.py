from django.urls import path
from Myapp import views

urlpatterns = [
    path('', views.home, name='my_home'),
    path('about/', views.about, name='my_about'),
    path('portfolio/', views.portfolio, name='my_portfolio'),
    path('do/', views.do, name='my_do'),
    path('contact/', views.contact, name='my_contact'),


]
