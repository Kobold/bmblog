import cherrypy

class Blog(object):
    def index(self):
        return "Hello world!"
    index.exposed = True

cherrypy.quickstart(Blog())
