"""FirebaseAuthProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include
from FirebaseAuthApp.views import user_register, user_login, home_page, password_reset, user_profile, user_logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name='home_page'),
    path('user_register/',user_register , name='user_register'),
    path('user_login/', user_login, name='user_login'),
    path('user_profile/', user_profile, name='user_profile'),
    path('password_reset/', password_reset, name='password_reset') ,
    path('user_logout/', user_logout, name='user_logout'),
    path('accounts/', include('django.contrib.auth.urls'))
]



