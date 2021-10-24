from django.shortcuts import render

# Create your views here.

'''
视图
所谓的视图就是python函数
视图函数有两个要求
    1.视图函数的第一个要求就是接收请求  这个请求其实就是 HttpRequest的类对象
    2.必须返回一个响应
'''
from django.http import HttpRequest,HttpResponse

#我们期望用户输入 http://127.0.0.1:8000/inedx/   来访问视图函数
def index(request):

    return HttpResponse("okokokokokokokokokok")