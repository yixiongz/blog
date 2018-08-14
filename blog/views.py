from django.shortcuts import render, redirect, HttpResponse
from .models import Bloginfo
# Create your views here.

def index(request):
    all_list = Bloginfo.objects.all()
    return render(request, "blog/blogs.html", {"all_list":all_list})


def blog_add(request):
    return render(request, "blog/blog_add.html")