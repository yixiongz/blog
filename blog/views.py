from django.shortcuts import render, redirect, HttpResponse
from .models import Bloginfo
# Create your views here.

def index(request):
    all_list = Bloginfo.objects.all()
    return render(request, "blog/blogs.html", {"all_list":all_list})


def blog_add(request):
    print(request.POST)
    if request.method == "POST":
        titled = request.POST.get("titled")
        author = request.POST.get("author")
        body = request.POST.get("body")
        if titled and author and body:
            Bloginfo.objects.create(title=titled,author=author,body=body)
            return redirect("/blog/index/")
        else:
            return render(request, "blog/blog_error.html")
    return render(request, "blog/blog_add.html")


def blog_del(request):
    del_id = request.GET.get("id")
    print(del_id)
    if del_id:
        Bloginfo.objects.get(id=del_id).delete()
    return redirect("/blog/index/")