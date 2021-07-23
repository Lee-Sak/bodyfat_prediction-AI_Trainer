"""fatpred URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import include, path

import fatapp.views

urlpatterns = [
    path('', fatapp.views.index, name='index'),
    path('child', fatapp.views.child, name='child'),
    path('childBasic', fatapp.views.childBasic, name='childBasic'),
    path('adult', fatapp.views.adult, name='adult'),
    path('adultBasic', fatapp.views.adultBasic, name='adultBasic'),
    path('senior', fatapp.views.senior, name='senior'),
    path('seniorBasic', fatapp.views.seniorBasic, name='seniorBasic'),
    path('childSubmit', fatapp.views.childSubmit, name='childSubmit'),
    path('adultSubmit', fatapp.views.adultSubmit, name='adultSubmit'),
    path('seniorSubmit', fatapp.views.seniorSubmit, name='seniorSubmit'),
    path('childBasicSubmit', fatapp.views.childBasicSubmit, name='childBasicSubmit'),
    path('adultBasicSubmit', fatapp.views.adultBasicSubmit, name='adultBasicSubmit'),
    path('seniorBasicSubmit', fatapp.views.seniorBasicSubmit, name='seniorBasicSubmit'),
    path('admin/', admin.site.urls),
]
