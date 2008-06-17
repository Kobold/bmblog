from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^bmblog/', 'posts.views.hello_world'),

    # Uncomment this for admin:
#     (r'^admin/', include('django.contrib.admin.urls')),
)
