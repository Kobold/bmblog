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
post_directory = os.environ['BMBLOG_POST_DIRECTORY']


def date(value, format='%B %e, %Y'):
    """Nice formatting for datetime strings."""
    return value.strftime(format)
environment.filters['date'] = date

def parse_files():
    md_files = [f for f in os.listdir(post_directory)
                if f.endswith('.markdown')]
    
    posts, pages = [], []
    for f in md_files:
        md = markdown.Markdown(extensions=['meta'])
        text = file(os.path.join(post_directory, f)).read().decode('utf-8')
        html = md.convert(text)
        
        type = md.Meta['type'][0]
        md_dict = {
            'title': md.Meta['title'][0],
            'slug': f[:-9], # slice off the .markdown to create the slug
            'body': html,
        }
        if type == 'post':
            md_dict.update({'date': dateutil.parser.parse(md.Meta['date'][0])})
            posts.append(md_dict)
        elif type == 'page':
            pages.append(md_dict)
    
    return posts, pages


class Blog(object):
    @cherrypy.expose
    def index(self):
        posts, pages = parse_files()
        posts = sorted(posts, key=operator.itemgetter('date'), reverse=True)
        template = environment.get_template('index.html')
        return template.render(first=posts[0], rest=posts[1:])
    
    @cherrypy.expose
    def post(self, slug):
        posts, pages = parse_files()
        post = dict((p['slug'], p) for p in posts)[slug]
        return environment.get_template('post.html').render(post=post)

configuration = {
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

if __name__ == '__main__':
    cherrypy.quickstart(Blog(), config=configuration)
