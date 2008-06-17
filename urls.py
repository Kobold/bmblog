from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^$', 'posts.views.main'),
    
    (r'^admin/', include('django.contrib.admin.urls')),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/Users/kobold/bmblog/static'}),
)
