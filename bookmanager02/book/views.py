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



############################## 修改数据 ##################################
#方法一
#相当于这句话select * from bookinfo where id = 6
book=BookInfo.objects.get(id=6)
book.name='运维开发入门'
book.name
book.save()  #保存数据


#方法二
# filter  过滤
BookInfo.objects.filter(id=6).update(name='爬虫入门',commentcount=666)

############################## 删除数据 ##################################

#删除分两种 物理删除(这条记录的数据删除) 和 逻辑删除(修改标记 例如is_delete=False)
#方法一
book=BookInfo.objects.get(id=6)
book.delete()
#方法二
BookInfo.objects.get(id=6).delete()
BookInfo.objects.filter(id=5).delete()


############################## 查询数据 ##################################
#get查询单一结果,如果不存在会抛出模型类.DoesNotExist异常
try:
    book=BookInfo.objects.get(id=1)
except BookInfo.DoesNotExist:
    print("查询结果不存在")

#all查询多个集结果
BookInfo.objects.all()
from book.models import PeopleInfo
PeopleInfo.objects.all()
#count查询结果数量
BookInfo.objects.all().count()
BookInfo.objects.count()

 ########################### 过滤查询 ##################################
# 实现SQL中的where功能，包括
# filter过滤出多个结果
# exclude排除掉符合条件剩下的结果
# get过滤单一结果
#语法形式
#模型类.objects.filter(属性名__运算符=值)   获取n个结果   n=0,1,2,...
#模型类.objects.exclude(属性名__运算符=值)    获取n个结果   n=0,1,2,...
#模型类.objects.get(属性名__运算符=值)        获取1个结果或者异常


# 查询编号为1的图书
book=BookInfo.objects.get(id=1)  #简写形式  (属性名=值)
book=BookInfo.objects.get(id__exact=1)    #完整形式 (id_exact=1)
BookInfo.objects.get(pk=1)   #pk primary key 主键
BookInfo.objects.filter(id=1)

# 查询书名包含'湖'的图书
BookInfo.objects.filter(name__contains='湖')
# 查询书名以'部'结尾的图书
BookInfo.objects.filter(name__endswith='部')
# 查询书名为空的图书
BookInfo.objects.filter(name__isnull=True)
# 查询编号为1或3或5的图书
BookInfo.objects.filter(id_in=[1,3,5])
# 查询编号大于3的图书
#大于  gt
#大于等于 gte
#小于  lt
#小于等于   lte
BookInfo.objects.filter(id_gt=3)
#查询编号不等于3的图书
BookInfo.objects.exclude(id=3)
# 查询1980年发表的图书
BookInfo.objects.filter(pub_date__year=1980)
# 查询1990年1月1日后发表的图书
BookInfo.objects.filter(pub_date__gt='1990-1-1')

########################### F对象 ##################################
#使用: 两个属性的比较
#语法形式 以filter为例 模型类名.objects.filter(属性名__运算符=F('第二个属性名'))
#查询阅读量大于等于评论量的图书
from django.db.models import F
BookInfo.objects.filter(readcount__gte=F('commentcount'))

########################### Q对象 ##################################

#并且查询
#查询阅读量大于20,并且编号小于3的图书
BookInfo.objects.filter(readcount__gt=20).filter(id__lt=3)
#或者
BookInfo.objects.filter(readcount__gt=20,id__lt=3)

#或者查询
#或者语法: 模型类名.objects.filter(Q(属性名__运算符=值)|Q(属性名__运算符=值)|...)
#并且语法: 模型类名.objects.filter(Q(属性名__运算符=值)&Q(属性名__运算符=值)&...)
#not 非 语法: 模型类名.objects.filter(~Q(属性名__运算符=值))
#查询阅读量大于20,或者id小于3的图书
from django.db.models import Q
BookInfo.objects.filter(Q(readcount__gt=20)|Q(id__lt=3))
#查询编号不等于3的图书
BookInfo.objects.filter(~Q(id=3))
