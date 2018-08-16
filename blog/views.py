from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .models import Bloginfo
from django.db.models import Max
from functools import wraps
# Create your views here.

def index(request):
    page_nums = request.GET.get("page")
    try:
        page_nums = int(page_nums)
    except Exception as E:
        page_nums = 1

    data_start = (page_nums-1)*10
    data_end = page_nums*10
    # 先获取数据库中的总长度
    page_count = Bloginfo.objects.all().count()
    pages, nums = divmod(page_count, 10)
    if nums:
        pages += 1

    all_list = Bloginfo.objects.all()[data_start:data_end]

    # 分组最大长度为11
    max_page = 11
    if pages < max_page:
        max_page = pages

    # 取分组最大长度的中间值
    helf_page = max_page // 2
    page_start = page_nums - helf_page   # 左边占一半
    page_end = page_nums + helf_page     # 右边占一半

    html_str_list = []
    if page_start <= 1:
        page_start = 1
        page_end = max_page

    if page_end > max_page:
        page_end = pages
        page_start = pages - max_page + 1

    if page_nums <= 1:
        html_str_list.append('<li class="disabled"><a href="#" aria-label="Previous"><span aria-hidden="true">上一页</span></a></li>')
    else:
        # 获取的get数减1
        html_str_list.append('<li ><a href="?page={}" aria-label="Previous"><span aria-hidden="true">上一页</span></a></li>'.format(page_nums-1))


    for i in range(page_start,page_end+1):
        tmp = '<li><a href="?page={0}" >{0}</a></li>'.format(i)
        html_str_list.append(tmp)

    if page_nums >= pages:
        html_str_list.append(
            '<li class="disabled"><a href="#" aria-label="Previous"><span aria-hidden="true">下一页</span></a></li>')
    else:
        # 获取的get数减1
        html_str_list.append(
            '<li ><a href="?page={}" aria-label="Previous"><span aria-hidden="true">下一页</span></a></li>'.format(
                page_nums + 1))

    page_html = "".join(html_str_list)
    return render(request, "blog/blogs_index.html", {"all_list":all_list,"page_html":page_html})


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






def blog_show(request,showid):
    showid = showid.split("/")
    # 如果获取到不存在的值，直接返回404页面
    bloginfo = get_object_or_404(Bloginfo, id=showid[0])
    return render(request,"blog/blog_show.html",{"bloginfo" : bloginfo})


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


