from django.urls import path
from . import views

urlpatterns = [
    #Главная
    path('',views.HomePageView.as_view(), name='home'),
    #path('',views.index, name='home'),



    #Навигация
    path('about', views.about, name='about'),


#материалы
    path('video', views.video, name='video'),
    path('materials', views.materials, name='materials'),
    path('lesmanager/', views.lesmanager, name='lesmanager'),


    path('books', views.books, name='books'),

    #уроки
    path('lesmanager/', views.lesmanager, name='lesmanager'),
    path('les/1/', views.les1, name='les1'),
    path('les/2/', views.les2, name='les2'),
]