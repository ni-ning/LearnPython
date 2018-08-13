from django.contrib import admin
from django.conf.urls import url
from app01 import views
from django.urls import path, re_path

urlpatterns = [
    path('index1/<int:num>/', views.index1, name='n1'),
    re_path(r'^index2/(\d+)/', views.index2, name='n2'),
    # url('admin/', admin.site.urls),
    # url('index/', views.index),
    # url('login/', views.login),
    # url('test/', views.test),
    # url('login_session/', views.login_session),
    # url('index_session/', views.index_session),
]
