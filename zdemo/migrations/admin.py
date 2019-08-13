from django.contrib import admin

# Register your models here.

# 管理站点

# 1 管理界面本地化
# 在settings.py中设置语言和时区
# LANGUAGE_CODE = 'zh-hans' # 使用中国语言
# TIME_ZONE = 'Asia/Shanghai' # 使用中国上海时间

# 2 创建管理员
# python manage.py createsuperuser

# 3 注册模型类
from .models import BookInfo, HeroInfo
admin.site.register(BookInfo)
admin.site.register(HeroInfo)


# 4 自定义管理页面
# 4.1 models.py 写函数并返回   4.2  再添加


# 4.3  调整列表页展示 7个操作
class BookInfoAdmin(admin.ModelAdmin):
    # 1 显示哪些字段  list_display
    list_display = ['btitle', 'bread', 'bcomment', 'bpub_date', 'MY DATE']
    # 2 每页显示的个数  list_per_page
    list_per_page = 2
    # 3 操作选项的位置  actions_on_top
    actions_on_bottom = True
    # 4 搜索框 search_fields 字段   paginator  分页器
    search_fields = ['btitle']
    # 6. 自定义列的名字  方法列 model.py—admin.py display = [‘read’]
    # 7. 关联对象


# 4.4 编辑页面操作
    # 4.4.1 显示字段
    # fields = ['btitle', 'bpub_date']
    # 4.4.2 分组显示
    fieldsets = (
        ('必填项', {'fields': ['btitle', 'bpub_date']}),
        ('选填项', {
            'fields': ['bread', 'bcomment'],
            'classes': ('collapse',)  # 是否折叠显示
        })
    )

    # 4.4.3 关联对象  块和表
    class BookInfoTabularInline(admin.TabularInline):
        # 表格个样式类
        model = HeroInfo
        extra = 1

    class BookInfoStackedInline(admin.StackedInline):
        # 块个样式类
        model = HeroInfo
        extra = 1


# 定义管理类需要继承自admin.ModelAdmin类
# 使用管理类有两种方式： 注册参数  装饰器
@admin.register(HeroInfo)
class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ['hname', 'hbook', 'read']
    # 5 右侧过滤器  list_filter
    list_filter = ['hgender']

admin.site.register(BookInfo, BookInfoAdmin)







