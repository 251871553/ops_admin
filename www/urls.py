from django.urls import path

from . import views
from django.views.generic import TemplateView

app_name = 'www'
urlpatterns = [
    path('', views.index, name='index'),
    #path('dump/', views.dump, name='dump'),
    path('files/', views.files, name='files'),
    path('download/', views.download, name='download'),
    path('welcome/', views.welcome, name='welcome'),
    path('demo/', views.demo, name='demo'),
    path('login/', views.login, name='login'),
    #path('login/', views.login, name='login'),
    path('dump/', TemplateView.as_view(template_name='www/jstack.html'), name="dump"),
    path('k8s/', TemplateView.as_view(template_name='www/k8s.html'), name="k8s"),
    path('Meter/', TemplateView.as_view(template_name='www/echarts8.html'), name="Meter"),
    path('热力图/', TemplateView.as_view(template_name='www/echarts7.html'), name="热力图"),
    path('k线图/', TemplateView.as_view(template_name='www/echarts6.html'), name="k线图"),
    path('雷达图/', TemplateView.as_view(template_name='www/echarts5.html'), name="雷达图"),
    path('饼图/', TemplateView.as_view(template_name='www/echarts4.html'), name="饼图"),
    path('地图/', TemplateView.as_view(template_name='www/echarts3.html'), name="地图"),
    path('拆线图2/', TemplateView.as_view(template_name='www/echarts2.html'), name="拆线图2"),
    path('拆线图1/', TemplateView.as_view(template_name='www/echarts1.html'), name="拆线图1"),
    path('home/', TemplateView.as_view(template_name='www/index.html'), name="home"),
]