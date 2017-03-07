from django.db import models
import random, string


class ArticleGroup(models.Model):
    name = models.CharField(max_length=32) # 分组名称

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Article(models.Model):
    title = models.CharField(max_length=100)  #标题
    category = models.CharField(max_length=50, blank=True) #标签
    date_time = models.DateField(auto_now_add=True)  #日期
    content = models.TextField(blank=True, null=True)  #正文
    is_prived = models.BooleanField(auto_created=False, null=False)  #是否为私有（True则不显示在目录中）
    # groupid = models.IntegerField(null=True)
    group = models.ForeignKey(ArticleGroup, null=True)

    def __str__(self):
        return self.title


    class Meta:
        ordering = ['-date_time']
class GroupPassword(models.Model):
    content = models.TextField(blank=False, null=False) # 密码内容
    group = models.ForeignKey(ArticleGroup,null=True)

    def __str__(self):
        return '*****'