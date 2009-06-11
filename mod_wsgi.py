# add a virtualenv to mod_wsgi's execution environment
import site
site.addsitedir('/home/admin/domains/boozeandmescaline.com/bmblog2-virtualenv/lib/python2.5/site-packages')

# add the directory with the blog module to our path
import sys
sys.path.append('/home/admin/domains/boozeandmescaline.com/bmblog2')

# configure the location of the posts directory
import os
os.environ['BMBLOG_POST_DIRECTORY'] = '/home/admin/domains/boozeandmescaline.com/bmblog-posts'

from blog import Blog, configuration
import cherrypy

sys.stdout = sys.stderr
cherrypy.config.update({'environment': 'embedded'})
application = cherrypy.Application(Blog(), config=configuration)
