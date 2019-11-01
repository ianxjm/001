from django.http import HttpResponse

def index(request):
    """
    视图：函数视图-》 以函数定义的视图
    :param request:  包含请求信息的请求对象
    :return:  HTTPResponse  相应对象
    """
    return HttpResponse("hello word")

def hello(request):
    return HttpResponse("I am fine,Thank you,and you?")