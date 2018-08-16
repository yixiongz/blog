#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.contrib import admin
from django.urls import path, re_path
from blog import views


urlpatterns = [
    path('index/', views.index, name="index"),
    path('blog_add/', views.blog_add, name="blogadd"),
    # path('blog_edit/', views.blog_edit, name="blogedit"),
    re_path(r"^blog_edit/(?P<editid>\d+/)$", views.blog_edit, name= "blogedit"),
    re_path(r"^blog_show/(?P<showid>\d+/)$", views.blog_show, name= "blogshow"),
    # path('blog_edit/', views.blog_edit, name="blogedit"),
    path('blog_del/', views.blog_del, name="blogdel"),
]
