#coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render
import datetime

from blog.models import Article


# def current_datetime(request):
#     now = datetime.datetime.now()
#     html = "<html><body> It is now %s. </body></html>" % now
#     return HttpResponse(html)

def home(request):
    info_dict = {'site':u'XY Blog', 'content':u'ABCDEFG'}
    return render(request, 'home.html', {'info_dict':info_dict})

# def book_list(request):
#     manager_list = Manager.objects.all()
#     for manager in manager_list:
#         print('get manager '+manager.name)
#     return render(request, 'home.html', {'manager_list':manager_list})

def get_directiory(request):
    list = []
    try:
        list = Article.objects.filter(is_prived=False)
    except Exception as e:
        list = ['啥也没找到']
    return render(request, 'directory.html', {'list':list})

def get_article(request, id):
    title = ''
    content = ''
    createtime = ''
    try:
        article = Article.objects.get(id=int(id))
        if article:
            title = article.title
            content = article.content
            content = content.split('\r\n')
            createtime = article.date_time
    except Exception as e:
        content = '翻遍了也没找到您要的东西 ==!'

    return render(request, 'article.html', {'title':title,'content':content,'createtime':createtime})