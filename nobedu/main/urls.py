from django.urls import path
from . import views

urlpatterns = [
    #Главная
    path('',views.index, name='home'),

    #материалы
    path('materials', views.materials, name='materials'),
    path('books', views.books, name='books'),
    path('books2', views.books2, name='books2'),
    path('materials', views.materials, name='materials'),
    path('materials', views.materials, name='materials'),

    #Навигация
    path('testmanager', views.testmanager, name='testmanager'),
    path('vocabulary', views.vocabulary, name='vocabulary'),
    path('about', views.about, name='about'),
    path('video', views.video, name='video'),

    #уроки
    path('lesmanager/', views.lesmanager, name='lesmanager'),
    path('les/1/', views.les1, name='les1'),
    path('les/2/', views.les2, name='les2'),
    path('les/3/', views.les3, name='les3'),
    path('les/4/', views.les4, name='les4'),
    path('les/5/', views.les5, name='les5'),
    path('les/6/', views.les6, name='les6'),
    path('les/7/', views.les7, name='les7'),
    path('les/8/', views.les8, name='les8'),
    path('les/9/', views.les9, name='les9'),
    path('les/10/', views.les10, name='les10'),


]