from django.urls import path

from . import views
app_name = 'ops_api'
urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.upload_file, name='upload_file'),
    #path('form/', views.k8s_api,name='k8s_api')
     path('form/', views.k8s_api, name='k8s_api')
]