from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^bmblog/', 'posts.views.main'),

    # Uncomment this for admin:
#     (r'^admin/', include('django.contrib.admin.urls')),
)
