from django.urls import path
from book.views import create_book,shop,register
urlpatterns=[
    path('create/',create_book),
    path('<city_id>/<shop_id>/',shop),
    path('register/',register)
]