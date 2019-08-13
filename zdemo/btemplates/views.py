from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View


class TemplateView(View):
    def get(self, request):
        # return HttpResponse('模板')
        context = {
            'age': 18,
            'name': '张三',
            'data_list': ['A', 'B', 'C', 'D'],
            'stu_dict': {
                'work': '优秀',
                'score': 99
            },
            'today_date': datetime.now(),
            'safe_data': '<a href="#">传智播客的网址</a>'
        }
        print(datetime.now())  # 2019-08-12 23:51:11.677022

        # 渲染模板文件
        return render(request, 'index.html', context=context)