from django.urls import path
from book.views import index
#固定搭配 urlpatterns = []
urlpatterns = [
    #path(路由,视图函数名)
    path('index/',index)
]