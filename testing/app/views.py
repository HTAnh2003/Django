from django.shortcuts import render
from django.http import HttpResponse
import datetime
import random


def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def random_trungthuong(request):
    people = ['Anh','Hien','Tuan','Juan','Trung','Huy','Hoa','Huong']
    name = random.choice(people)
    html = "<html><body>Chúc mừng %s đã trúng thưởng</body></html>" % name
    return HttpResponse(html)

def random_love(request):
    people = ['Hiên','Tuấn','Năng Anh','Kiệt','Trí','Mạnh']
    A, B = random.sample(people, 2)
    html = "<html><body>Bạn %s yêu bạn %s </body></html>" % (A,B)
    return HttpResponse(html)
