from django.http import HttpResponse,JsonResponse
from django.shortcuts import render, redirect
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
    # response = HttpResponse('res',status=200)
    # response['name'] = 'itcast'
    # return response
    # JSON --> dict
    #dict  --> JSON
    info = {
        'name':'itcast',
        'address':'shunyi'
    }
    girl_firend =[
        {
            'name': 'rose',
            'address': 'shunyi'
        },
        {
            'name': 'jack',
            'address': 'changping'
        }
    ]

    #data 返回的响应数据 一般是字典类型
    '''
    safe = True 是表示 我们data是字典数据
    JsonResponse  可以把字典转换为json
    
    现在给一个非字典数据,出了问题我们自己负责
    '''
    #json.loads --> JSON字符串转换为字典
    #json.dump  --> 将字典转换为字符串
    # response = JsonResponse(data=girl_firend,safe=False)
    # return response


    return redirect('http://www.itcast.cn')

    # import json
    # data = json.dumps(girl_firend)
    #
    # response = HttpResponse(data)
    # return response


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


'''
第一次请求,携带查询字符串
http://127.0.0.1:8000/set_cookie/?username=itcast&password=123
服务器接收到请求之后,获取username,服务器设置cookie信息,cookie信息包括 username
浏览器接收到服务器的响应后,应该把cookie信息保存起来

第二次及其之后的请求,我们访问http://127.0.0.1:8000/set_cookie/都会携带cookie信息,服务器就可以读取cookie信息,来判断用户身份

'''


def set_cookie(request):

    #获取查询字符串数据
    username=request.GET.get("username")
    password=request.GET.get("password")
    #服务器设置cookie信息
    #通过响应对象.set_cookie 方法
    response = HttpResponse('set_cookie')
    #key value=''
    # max_age 是一个秒数 从响应开始 记数的一个秒数
    response.set_cookie('name',username,max_age=60)
    response.set_cookie('psd',password)

    #删除cookie
    response.delete_cookie('psd')
    return response

def get_cookie(request):
    #获取cookie信息
    print(request.COOKIES)

    #request.COOKIES  字典数据
    name=request.COOKIES.get('name')
    return HttpResponse(name)


################################################
#session 是保存在服务端
#session 依赖于cookie

'''
第一次请求 http://127.0.0.1/set_session/?userename=itheima  我们在服务器端设置session信息
服务器同时会成生一个session的 cooike信息
浏览器接收到这个信息后,会把cookie信息保存起来

第二次及其中之后的请求 都会携带这个session ,服务器会验证这个sessionid,验证没问题会读取相关数据.实现业务逻辑
'''


def set_session(request):

    #1 模拟 获取用户信息
    username = request.GET.get('username')

    #设置session信息
    #假如 我们通过模型查询 查到了用户信息
    user_id=1

    request.session['user_id']=user_id
    request.session['username']=username

    #clear 删除session里的数据,但是key保留
    # request.session.clear()
    #flush 是删除所有的数据 包括key
    # request.session.flush()

    request.session.set_expiry(60)
    return HttpResponse('set_session')


def get_session(request):

    # user_id=request.session['user_id']
    # username=request.session['username']

    user_id=request.session.get('user_id')
    username=request.session.get('username')
    # "%s"%username
    content = '{},{}'.format(user_id,username)

    return HttpResponse(content)


def login(request):
    print(request.method)
    if request.method == 'GET':
        return HttpResponse("get 逻辑")
    elif request.method == 'POST':
        return HttpResponse("POST 逻辑")

"""
类视图的定义
class 类视图名字(View):
    def get(self,request):
        return HttpResponse("xxx")
    def http_method_lower(self,request):
        return HttpResponse("xxx")
1. 继承View
2.类视图中的方法 是采用和 http方法小写来区分不同的请求方式
"""

from django.views import View
class LoginView(View):
    def get(self,request):

        return HttpResponse("get get get")

    def post(self, request):

        return HttpResponse("post post post")