from django.db import models

# Create your models here.

# 博客信息表
class  Bloginfo(models.Model):
    #  博客名称， 博客作者， 博客内容
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=25)
    body = models.TextField()

    def __str__(self):
        return self.title