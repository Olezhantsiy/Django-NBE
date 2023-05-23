from django.urls import path
from . import views

urlpatterns = [
    path('', views.testmanager, name='testmanager'),
    path('test1/', views.test1, name='test1'),
    path('test2/', views.test2, name='test2'),
    path('test3/', views.test3, name='test3'),
    path('test4/', views.test4, name='test4'),
    path('test5/', views.test5, name='test5'),
    path('addQuestion/', views.addQuestion, name='addQuestion'),

]