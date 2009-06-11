# -*- coding: utf-8 -*-
from jinja2 import Environment, FileSystemLoader
import cherrypy
import dateutil.parser
import markdown
import operator
import os


PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
TEMPLATE_ROOT = os.path.join(PROJECT_ROOT, 'templates')


environment = Environment(loader=FileSystemLoader(TEMPLATE_ROOT))
posts = [] # in memory list of posts that is loaded at startup


def date(value, format='%B %e, %Y'):
    """Nice formatting for datetime strings."""
    return value.strftime(format)
environment.filters['date'] = date


class Blog(object):
    @cherrypy.expose
    def index(self):
        template = environment.get_template('index.html')
        return template.render(posts=posts)


# load the posts on startup
post_directory = os.environ['BMBLOG_POST_DIRECTORY']
post_files = [f for f in os.listdir(post_directory)
                if f.endswith('.markdown')]
for f in post_files:
    md = markdown.Markdown(extensions=['meta'])
    text = file(os.path.join(post_directory, f)).read().decode('utf-8')
    html = md.convert(text)
    posts.append({
        'title': md.Meta['title'][0],
        'date': dateutil.parser.parse(md.Meta['date'][0]),
        'body': html,
    })
    
    # display posts nicely in chronological order
    posts.sort(key=operator.itemgetter('date'), reverse=True)

if __name__ == '__main__':
    conf = {
        '/': {
            'tools.encode.on': True,
            'tools.encode.encoding': 'utf8',
            'tools.staticdir.root': PROJECT_ROOT
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': 'static',
        },
    }
    cherrypy.quickstart(Blog(), config=conf)
