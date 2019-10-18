from django.urls import path

from . import views

app_name = 'www'
urlpatterns = [
    path('', views.index, name='index'),
    path('dump/', views.dump, name='dump'),
    path('files/', views.files, name='files'),
    path('download/', views.download, name='download'),
    path('welcome/', views.welcome, name='welcome'),
    path('demo/', views.demo, name='demo'),
    path('login/', views.login, name='login'),
    #path('login/', views.login, name='login'),
]