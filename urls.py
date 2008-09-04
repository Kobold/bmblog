from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'posts.views.main'),
    (r'^feed/$', 'posts.views.feed'),
    (r'^post/([a-z-]+)/$', 'posts.views.post'),
    
    (r'^admin/(.*)', admin.site.root),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/Users/kobold/bmblog/static'}),
)
