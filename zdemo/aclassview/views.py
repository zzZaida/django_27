from django.http import HttpResponse
from django.shortcuts import render

from django.utils.decorators import method_decorator  # utils --> 工具类

from django.views import View

# 定义装饰器
def my_decorator(func):
    def wrapper(request, **kwargs):
        print('添加装饰器-----', request.method)
        return func(request, **kwargs)
    return wrapper


# @method_decorator(my_decorator,name='get')
@method_decorator(my_decorator, name='dispatch')  # --> 经手的dispatch都加装饰器
# --> 负责将 IndexView 中的函数弄出来
# ValueError: The keyword argument `name` must be the name of a method of the decorated  Got '' instead
# 定义类视图
class IndexView(View):

    # @my_decorator  --> 报错：wrapper() takes 1 positional argument but 2 were given
    # 对象方法
    # @method_decorator(my_decorator)  # --> 一个添加  其他不添加装饰器
    def get(self, request):
        return HttpResponse('method_decorator------register.html')

    def post(self, request):
        return HttpResponse('method_decorator-------这里实现注册逻辑')

def index(request):
    # 获取请求方法，判断是GET/POST请求
    if request.method == 'GET':
        # 处理GET请求，返回注册页面
        return render(request, 'register.html')
    else:
        # 处理POST请求，实现注册逻辑
        return HttpResponse('这里实现注册逻辑')