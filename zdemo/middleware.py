
def simple_middleware(get_response):
    # 此处编写的代码仅在Django第一次配置和初始化的时候执行一次。
    print('-----init---DEBUG模式下 init调用两次----1111111111')

    def middleware(request):
        # 此处编写的代码会在每个请求处理视图前被调用。
        # 1.屏蔽IP 爬虫非正常用户访问 2.判断是否登录
        print('处理请求对象之前---屏蔽IP--1111111')
        response = get_response(request)

        # 此处编写的代码会在每个请求处理视图之后被调用。
        print('处理请求对象之后---------1111111')
        return response

    return middleware


# 中间件的执行顺序:处理请求对象之前: 从上到下   MIDDLEWARE = []
#               处理请求对象之后: 从下到上
def simple_middlewareTwo(get_response):
    print('-----init---DEBUG模式下 init调用两次----2222222')

    def middleware(request):

        print('处理请求对象之前---屏蔽IP--22222222')
        response = get_response(request)

        print('处理请求对象之后---------222222222')
        return response

    return middleware


# 处理请求对象之前---屏蔽IP--1111111
# 处理请求对象之前---屏蔽IP--22222222
# 添加装饰器----- GET
# 处理请求对象之后---------222222222
# 处理请求对象之后---------1111111
