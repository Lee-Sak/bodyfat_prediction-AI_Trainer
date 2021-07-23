from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('child', views.child, name='child'),
    path('childBasic', views.childBasic, name='childBasic'),
    path('adult', views.adult, name='adult'),
    path('adultBasic', views.adultBasic, name='adultBasic'),
    path('senior', views.senior, name='senior'),
    path('seniorBasic', views.seniorBasic, name='seniorBasic'),
    path('childSubmit', views.childSubmit, name='childSubmit'),
    path('adultSubmit', views.adultSubmit, name='adultSubmit'),
    path('seniorSubmit', views.seniorSubmit, name='seniorSubmit'),
    path('childBasicSubmit', views.childBasicSubmit, name='childBasicSubmit'),
    path('adultBasicSubmit', views.adultBasicSubmit, name='adultBasicSubmit'),
    path('seniorBasicSubmit', views.seniorBasicSubmit, name='seniorBasicSubmit'),

]