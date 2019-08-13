
# template提供的内置过滤器，不够用，不灵活，就可以自己定义一个过滤器

# 3 导包template
from django import template

# 4 实例化注册对象
register = template.Library()

# 5 使用装饰器自定义过滤器
@register.filter
def odd(x):
    return x / 3


