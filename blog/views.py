from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .models import Bloginfo
from django.db.models import Max
# Create your views here.

def index(request):
    all_list = Bloginfo.objects.all()
    return render(request, "blog/blogs_index.html", {"all_list":all_list})


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


# 编辑
def blog_edit(request,editid):
    editid = editid.split("/")
    # 如果获取到不存在的值，直接返回404页面
    bloginfo = get_object_or_404(Bloginfo, id=editid[0])

    if request.method == "POST":
        titled = request.POST.get("titled")
        author = request.POST.get("author")
        body = request.POST.get("body")
        if titled and author and body:
            bloginfo.title = titled
            bloginfo.author = author
            bloginfo.body = body
            bloginfo.save()
            return redirect("/blog/index/")
        else:
            # 当输入框为空的时候，点击返回，重新填写
            return render(request, "blog/blog_edit_error.html",{"bloginfo":bloginfo})

    # 获取数据库中的id最大序列号
    blog_count = Bloginfo.objects.all().aggregate(max = Max("id"))
    if int(editid[0]) > blog_count["max"]:
            return render(request, "blog/blog_error.html")

    return render(request, "blog/blog_edit.html",{"bloginfo":bloginfo})

# 博客删除功能
def blog_del(request):
    # 获取ID
    del_id = request.GET.get("id")
    # 如果存在就删除，不存在 直接返回主界面
    if del_id:
        try:
            Bloginfo.objects.get(id=del_id).delete()
        except Exception as E:
            return redirect("/blog/index/")
    return redirect("/blog/index/")