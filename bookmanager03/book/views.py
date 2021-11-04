from django.http import HttpResponse
from django.shortcuts import render
from book.models import BookInfo

# Create your views here.
def create_book(request):
    book=BookInfo.objects.create(
        name='abc',
        pub_date='2020-1-1',
        readcount=10
    )
    return HttpResponse('create')

def shop(request,city_id,shop_id):

    # print(city_id,shop_id)
    query_params = request.GET
    # print(query_params)
    # order = query_params.get('order')
    # print(order)
    # order = query_params['order']
    # print(order)
    order = query_params.getlist('order')
    print(order)
    return HttpResponse('齐哥的小饭店')

def register(requset):
    data=requset.POST
    print(data)
    return HttpResponse('ok')

def json(request):

    # request.POST  json数据不能通过request.POST获取数据
    body=request.body
    body_str=body.decode()
    # print(body_str)

    #JSON形式的字符串 可以转换为Python的字典
    import json
    body_dict=json.loads(body_str)
    # print(body_dict)

    ###########请求头###########
    print(request.META['SERVER_PORT'])

    return HttpResponse("json")


def method(request):
    print(request.method)
    return HttpResponse('method')

def response(request):
    response = HttpResponse('res',status=200)
    response['name'] = 'itcast'
    return response
    #1xx
    #2xx
    # 200 成功
    #3xx
    #4xx  请求有问题
    #404  找不到页面  路由有问题
    #403  403禁止访问  权限问题
    #5xx
    # 响应状态码100~599
    return HttpResponse('response',status=404)
