"""XYBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from blog import views as blog_views

urlpatterns = [
    url(r'^$',blog_views.home, name='home'),
    url(r'^home/', blog_views.home, name='home'),
    url(r'^login/$', blog_views.login),
    url(r'^article/(\d+)/$', blog_views.get_article),
    url(r'^dir/$', blog_views.get_directiory),
    url(r'^admin/', admin.site.urls, name='admin'),
    # url(r'^static/(?P<path>.*)$',django.views.static.serve,{'document_root':settings.STATIC_ROOT}),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
