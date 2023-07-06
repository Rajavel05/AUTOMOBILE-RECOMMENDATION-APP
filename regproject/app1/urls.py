"""regproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views
urlpatterns = [
    path('',views.SignupPage,name='signup'),
    path('home/', views.HomePage, name='home'),
    path('about/', views.about , name='about'),
    path('login/',views.LoginPage,name='login'),
    path('logout/',views.LogoutPage,name='logout'),
    path('dealer/', views.dealer, name='dealer'),
    path('explore/', views.tata, name='explore'),
    path('explore1/', views.mahen, name='explore1'),
    path('explore2/', views.kia, name='explore2'),
    path('dealer2/', views.dealer2, name='dealer2'),
    path('dealer3/', views.dealer3, name='dealer3'),
]


