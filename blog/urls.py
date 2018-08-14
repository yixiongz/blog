#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.contrib import admin
from django.urls import path
from blog import views


urlpatterns = [
    path('index/', views.index, name="index"),
    path('blog_add/', views.blog_add, name="blogadd"),
]
