from django.db import models


# # 自定义 manage 管理器
# class BookInfoManage(models.Manager):
#
#     # 1 修改系统的函数满足自己的需求
#     def all(self):
#         return super().filter(is_delete=False)
#
#     # 2 添加新功能
#     def create_book(self,title, date):
#         book = self.model()
#         book.btitle = title
#         book.bpub_date = date
#         book.save()


#  模型类 ---表
#  属性   字段
class Person(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField(default=18)
    gender = models.BooleanField(default=0)

    class Meta:
        # 修改表的名字
        db_table = 'a_person'


class PersonOne(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField(default=18)
    gender = models.BooleanField(default=0)


from django.db import models


#定义图书模型类BookInfo
class BookInfo(models.Model):

    # 自定义管理器实例化
    # books = BookInfoManage()

    btitle = models.CharField(max_length=20, verbose_name='名称')
    bpub_date = models.DateField(verbose_name='发布日期')
    bread = models.IntegerField(default=0, verbose_name='阅读量')
    bcomment = models.IntegerField(default=0, verbose_name='评论量')
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')

    # 新增图片字段    null=True 兼容老数据  以前数据没有图片
    # upload_to 选项指明该字段的图片保存在MEDIA_ROOT目录中的哪个子目录
    image = models.ImageField(upload_to="pictures", null=True)

    class Meta:
        db_table = 'tb_books'  # 指明数据库表名
        verbose_name = '图书'  # 在admin站点中显示的名称
        verbose_name_plural = verbose_name  # 显示的复数名称  图书s

    def __str__(self):
        """定义每个数据对象的显示信息"""
        return self.btitle

    # 自定义日期
    def my_date(self):

        return self.bpub_date.strftime('%Y-%m-%d')
    my_date.short_description = "我的日期"
    my_date.admin_order_field = "bpub_date"


#定义英雄模型类HeroInfo
class HeroInfo(models.Model):
    # 枚举  英文用户看--> 0 1 给数据库
    GENDER_CHOICES = (
        (0, 'female'),
        (1, 'male')
    )
    hname = models.CharField(max_length=20, verbose_name='名称')
    hgender = models.SmallIntegerField(choices=GENDER_CHOICES, default=0, verbose_name='性别')
    hcomment = models.CharField(max_length=200, null=True, verbose_name='描述信息')
    # 外键属性
    # hbook = models.ForeignKey(BookInfo, on_delete=models.CASCADE, verbose_name='图书', related_name='subs')  # 外键
    hbook = models.ForeignKey(BookInfo, on_delete=models.CASCADE, verbose_name='图书')  # 外键
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')

    class Meta:
        db_table = 'tb_heros'
        verbose_name = '英雄'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.hname

    # 7 关联对象的属性或方法
    def read(self):
        return self.hbook.bread

    read.short_description = '图书阅读量'
