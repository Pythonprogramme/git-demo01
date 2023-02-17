"""gitdemo01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# 引入 include
from django.urls import include

# 引入三个app的 views
# from apps.basicweb import views as basic_views
# from apps.mainweb import views as main_views
# from apps.orderweb import views as order_views

urlpatterns = [
    path('admin/', admin.site.urls),
#   基础数据
    path('basic/', include('basicweb.urls')),
#   用户角色
    path('main/', include('mainweb.urls')),
#   订单管理
    path('order/', include('orderweb.urls')),
#   登录账号
    path('user/', include('userweb.urls'))
]
