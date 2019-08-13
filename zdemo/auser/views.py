from django.http import HttpResponse
from django.shortcuts import render


# Django也用视图来编写Web应用的业务逻辑。
# Django的视图是定义在子应用的views.py中的。

# Create your views here.
from django.urls import reverse


def index(request):
    """
    index 视图
    :param request: 包含了请求信息的请求对象
    :return: 响应对象
    """
    return HttpResponse('Hello World!!')



