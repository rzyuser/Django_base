from django.db import models

# Create your models here.
from django.http import HttpResponse
'''
1. 模型类 需要继承自 model.Model
2. 定义属性
        id 系统会默认生成
        属性名=model.类型(选项)
        2.1 属性名 对应就是字段名
            不要使用关键字
        2.2 类型 MySQL的类型
        2.3选项 是否有默认值, 是哦否唯一,是否为null
                CharFiled 必须设置 max_length
                varbose_name 主要是 admin站点使用
3. 改变表的名字
    默认表的名称是 子应用名_类名  都是小写
    修改表的名字   class Meta
create table 'qq_user'(
    id int
    name varchar(10) not null default '' 
)
'''
class BookInfo(models.Model):
    name=models.CharField(max_length=10,unique=True)   #unipue  是否不重名 True为不重名
    pub_date=models.DateField(null=True)
    readcount=models.IntegerField(default=0)
    commentcount=models.IntegerField(default=0)
    is_delete=models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table='bookinfo'       #修改表名
        verbose_name='书籍管理'        #admin站点使用的


class PeopleInfo(models.Model):
    # 定义一个有序字典
    GENDER_CHOICE = (
        (1,'male'),
        (2,'female')
    )
    name=models.CharField(max_length=10,unique=True)
    gender=models.SmallIntegerField(choices=GENDER_CHOICE,default=1)
    description=models.CharField(max_length=100,null=True)
    is_delete=models.BooleanField(default=False)

    #外健
    #系统会自动为外健添加_id

    #外健的级联操作
    # 主表 和 从表
    # 1 对 多
    # 书籍  对  人物
    book = models.ForeignKey(BookInfo,on_delete=models.CASCADE)

    class Meta:
        db_table='peopleinfo'       #修改表名

    def __str__(self):
        return self.name