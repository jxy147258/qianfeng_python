from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


# 定义了一个视图，也就是一个html页面
def index(request):
    return HttpResponse("sunck is a good man !")