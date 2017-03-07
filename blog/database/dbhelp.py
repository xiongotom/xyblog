from blog.models import Article, ArticleGroup, GroupPassword

class singleton(object):
    def __new__(cls, *args, **kwargs):
        if '_inst' not in vars(cls):
            cls._inst = super(singleton, cls).__new__(cls, *args, **kwargs)
        return cls._inst

class Dbhelp(singleton):
    defautl_list = ['啥也没找到']

    ''' 根据分组id获取文章列表（默认返回所有公开的文章列表） '''
    def get_article_list(self, groupid=-1):
        list = []
        try:
            if groupid==-1:
                list = Article.objects.filter(is_prived=False)
            else:
                list = Article.objects.filter(is_prived=False, group_id=groupid)
        except Exception as e:
            list = self.defautl_list
        return list

    ''' 根据暗号获取文章列表 '''
    def get_artcle_list_by_password(self, password=''):
        try:
            pwd_list = GroupPassword.objects.filter(content=password)
            if len(pwd_list)==1:
                artcle_list = Article.objects.filter(group_id=pwd_list[0].groupid)
                return artcle_list
        except Exception as e:
            print(str(e))
        return self.defautl_list
