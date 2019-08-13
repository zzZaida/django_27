from django.shortcuts import render

from django.views import View
from .models import BookInfo, HeroInfo
from datetime import date


class ModelsView(View):
    # 查询   get()   all()
    def get(self, request,):
        book = BookInfo.objects.get(id=1)
        # 查询所有
        books = BookInfo.objects.all()
        context = {
            # 'books':[book],
            'books': books
        }
        # 渲染模板文件
        # return render(request, '../templates/index1.html')
        return render(request, 'index1.html',context)

    # 增加 post --- save()   create()
    def post(self,request):
        book = BookInfo()
        book.btitle = '黄皮子坟'
        book.bpub_date = date(1990, 1, 1)
        book.save()

        BookInfo.objects.create(
            btitle='黄皮子坟',
            bpub_date=date(1990, 1, 1)
        )
        return render(request, 'index1.html',context={'add':'添加成功！'})

    # 删除  delete --- delete()  filter()
    def delete(self, request):
        book = BookInfo.objects.get(id=6)
        book.delete()

        # 取出直接删除
        BookInfo.objects.filter(id=7).delete()
        return render(request, 'index1.html',context={'add':'删除成功！'})

    # 修改  put ---- save()   update()
    def put(self, request):
        book = BookInfo.objects.get(id=5)
        book.btitle = '鬼吹灯'
        book.save()

        # 取出直接改  exclude() <====>  !=
        BookInfo.objects.filter(id=5).update(btitle='黄河鬼棺')
        return render(request, 'index1.html',context={'add':'修改成功！'})



# python manage.py shell
# 2   过滤查询   属性名字__符号 = 值   filter() get() exclude()

from migrations.models import BookInfo, HeroInfo

# 2.1 相等      exact  不等exclude()   <QuerySet>查询集
BookInfo.objects.filter(id__exact=4)
BookInfo.objects.exclude(id__exact=4)
# 2.2条件运算    gt lt gte lte
BookInfo.objects.filter(id__lt=2)
# 2.3 范围       in
BookInfo.objects.filter(id__in=[2, 1, 5])
# 2.4 判空       isnull
BookInfo.objects.filter(btitle__isnull=False)
# 2.5 模糊查询    contains startswith endswith
BookInfo.objects.filter(btitle__contains='江')
BookInfo.objects.filter(btitle__start='雪')
# 2.6 日期       year ,month,day
BookInfo.objects.filter(bpub_date__year=1990)
BookInfo.objects.filter(bpub_date__gt=date(1990, 1, 1))


# 3
# F对象 ---> 多属性对比
from django.db.models import F, Q

BookInfo.objects.filter(bpub_date__gt=F('bcomment'))
# Q对象 -->多条件查询 - - 与( &) 或( |) 非(~)
# 查询阅读量大于20，并且编号小于3的图书。
# BookInfo.objects.filter(Q(id__lt=3) & Q(bread__gt=20))
BookInfo.objects.filter(id__lt=3, bread__gt=20)
BookInfo.objects.filter(Q(id__lt=3) | Q(bread__gt=20))
BookInfo.objects.filter(~Q(id__lt=3))


# 4 聚合查询  aggregate()
# Sum Avg Max Min Count
from django.db.models import Sum, Avg, Max, Min, Count
BookInfo.objects.aggregate(Sum('bread'))
BookInfo.objects.aggregate(Count('id'))  # {'id__count': 5}
BookInfo.objects.count() # 5
BookInfo.objects.filter(id__lt=3).count()


# 5 排序 order_by('id') 升序
# order_by('-id') 降序
BookInfo.objects.order_by(id__lt=3)


# 6 关联查询  1:n   n:1
# 1:n  书：英雄   关联模型类小写_set
# 查找 id=3 的书里的所有英雄
book = BookInfo.objects.get(id=3)
# 关联模型类小写_set
book.heroinfo_set.all()
# 或者   book.subs.all()

# n:1
# 乔峰是哪本书中的英雄
hero = HeroInfo.objects.get(hname="乔峰")
# hero.hbook  # <BookInfo:天龙八部>

# 关联过滤查询
# 1：n               关联模型类小写__属性名字__运算符 = 值
BookInfo.objects.filter(heroinfo__hname__exact='袁紫衣')
# BookInfo.objects.filer(subs__hname__exact='袁紫衣')
# n:1
HeroInfo.objects.filter(hbook__btitle__exact="天龙八部")


# 7 查询集querySet 的特点： filter() all() order_by() exclude()
# 7.1 惰性执行  懒加载：等需要操作数据的时候  才交互数据库--> 减少读写操作
# 7.2 缓存--> 减少读写操作  提高CPU效率
q = BookInfo.objects.filter(id=2)
qs = BookInfo.objects.all()
[book for book in qs]
# [book for book in qs]   在缓存失效之前  不交互数据库


# 8 自定义 manage 管理器   1 添加新功能  2 修改系统的函数满足自己的需求
# object ==系统自带的管理器
# is_delete = 1
from migrations.models import BookInfo, HeroInfo
BookInfo.books.all()
BookInfo.books.create_book("长安",date(2019, 1, 1))




