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
    path('权限管理/', TemplateView.as_view(template_name='www/admin-rule.html'), name="权限管理"),
    path('权限分类/', TemplateView.as_view(template_name='www/admin-cate.html'), name="权限分类"),
    path('角色管理/', TemplateView.as_view(template_name='www/admin-role.html'), name="角色管理"),
    path('管理员列表/', TemplateView.as_view(template_name='www/admin-list.html'), name="管理员列表"),
    path('三级地区联动/', TemplateView.as_view(template_name='www/city.html'), name="三级地区联动"),
    path('多级分类/', TemplateView.as_view(template_name='www/cate.html'), name="多级分类"),
    path('订单列表1/', TemplateView.as_view(template_name='www/order-list1.html'), name="订单列表1"),
    path('订单列表/', TemplateView.as_view(template_name='www/order-list.html'), name="订单列表"),
    path('等级管理/', TemplateView.as_view(template_name='www/member-list1.html'), name="等级管理"),
    path('会员删除/', TemplateView.as_view(template_name='www/member-del.html'), name="会员删除"),
    path('会员列表动态表格/', TemplateView.as_view(template_name='www/member-list1.html'), name="会员列表动态表格"),
    path('会员列表静态表格/', TemplateView.as_view(template_name='www/member-list.html'), name="会员列表静态表格"),
 #   path('会员列表静态表格/', TemplateView.as_view(template_name='www/member-list.html'), name="会员列表静态表格"),
    path('home/', TemplateView.as_view(template_name='www/index.html'), name="home"),
]