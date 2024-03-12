from django.urls import path
from .views import current_datetime,random_trungthuong,random_love #.view vì view.py nằm cùng thư mục với urls.py
urlpatterns = [
    path("time/", current_datetime, name="current_datetime"),
    path("random/", random_trungthuong, name="random_trungthuong"),
    path("love/", random_love, name="random_love"),
]
