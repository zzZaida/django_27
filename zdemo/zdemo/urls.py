"""zdemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin


from auser import urls

# urlpatterns是被django自动识别的路由列表变量
from auser import views

urlpatterns = [

    # 每个路由信息都需要使用url函数来构造
    # url(路径, 视图)
    url(r'^admin/', admin.site.urls),
    # url(r'^', include(urls)),
    # 总路由--->子路由
    # include函数除了可以传递字符串之外，也可以直接传递应用的urls模块，
    # url(r'^', include("auser.urls", namespace='auser')),


    # 类视图
    url(r'^', include('aclassview.urls')),

    # 模板
    url(r'^', include('btemplates.urls')),


    url(r'^', include('migrations.urls')),


]
