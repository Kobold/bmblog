from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^$', 'posts.views.main'),
    
    (r'^admin/', include('django.contrib.admin.urls')),
)
