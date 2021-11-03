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