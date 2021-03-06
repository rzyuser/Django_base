from django.db import models

# Create your models here.
#创建书籍信息
class BookInfo(models.Model):
    #id
    name = models.CharField(max_length=10)
    # 重写str 方法让admin来显示书籍名字
    def __str__(self):
        return self.name

#人物
class PeopleInfo(models.Model):
    name=models.CharField(max_length=10)
    gender=models.BooleanField()
    #外健约束:人物属于哪本书
    book = models.ForeignKey(BookInfo,on_delete=models.CASCADE)