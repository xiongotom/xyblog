from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=100)  #标题
    category = models.CharField(max_length=50, blank=True) #标签
    date_time = models.DateField(auto_now_add=True)  #日期
    content = models.TextField(blank=True, null=True)  #正文

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_time']