from django.contrib import admin

# Register your models here.
from blog.models import *

admin.site.register(Article)
admin.site.register(ArticleGroup)
admin.site.register(GroupPassword)
