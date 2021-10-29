from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from book.models import BookInfo


def index(request):

    #在这里实现  增删改查
    book=BookInfo.objects.all()
    print(book)
    return HttpResponse('index')


###########################增加数据#######################
from book.models import BookInfo
#方式一
book=BookInfo(
    name='Django',
    pub_date='2000-1-1',
    readcount=10,
)
#必须调用对象的save方法才能将数据保存到数据库中
book.save()

#方法二    直接就可以添加到数据库
BookInfo.objects.create(
    name='测试开发入门',
    pub_date='2020-1-1',
    readcount=100,
)