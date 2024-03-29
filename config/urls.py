"""config URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from clearskin import views as views_py
from authtest.views import HomeView ,UserCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views_py.home, name="home"),
    path('authtest/', include('authtest.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', UserCreateView.as_view(), name="signup"),
    path('clearskin/', views_py.index, name="index"),
    path('recipe/', views_py.recipe, name="recipe"),
    path('score', views_py.score, name="score"),

]
