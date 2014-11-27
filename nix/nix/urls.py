from django.conf.urls import patterns, include, url
from django.contrib import admin
from posts import views as post_views

urlpatterns = patterns('',
    # url(r'^$', 'nix.views.home', name='home'),
    url(r'^$', include('posts.urls')),
    url(r'^post/', post_views.post, name='post'),
    url(r'^order/', post_views.order, name='order'),
    url(r'^printers/', include('printers.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^pages/', include('django.contrib.flatpages.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
