# add a virtualenv to mod_wsgi's execution environment
import site
site.addsitedir('/home/admin/domains/boozeandmescaline.com/bmblog2-virtualenv/lib/python2.5/site-packages')

from blog import Blog
import cherrypy
import sys
sys.stdout = sys.stderr

cherrypy.config.update({'environment': 'embedded'})
application = cherrypy.Application(Blog(), None)
