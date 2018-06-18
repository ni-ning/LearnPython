from django.contrib import admin
from django.conf.urls import url
from app01 import views

urlpatterns = [
    url('admin/', admin.site.urls),
    url('index/', views.index),
    url('login/', views.login),
    url('test/', views.test),
    url('login_session/', views.login_session),
    url('index_session/', views.index_session),
]
