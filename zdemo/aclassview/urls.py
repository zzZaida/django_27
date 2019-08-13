from django.conf.urls import url

from aclassview.views import my_decorator
from . import views

urlpatterns = [
    # 子路由 --> 视图函数
    # url(r'^classview/$',views.index),

    # 子路由 -IndexView-> 视图函数
    # as_view() 作用：将类视图的对象方法  根据请求方式返回
    url(r'^classview/$', views.IndexView.as_view()),

    # 类视图添加装饰器方法一
    # url(r'^classview/$', views.my_decorator(views.IndexView.as_view())),
    # url(r'^classview/$', my_decorator(views.IndexView.as_view())),

]