# -*- coding: utf-8 -*-
from jinja2 import Environment, FileSystemLoader
import cherrypy
import markdown
import os

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
ENVIRONMENT = Environment(
    loader=FileSystemLoader(os.path.join(PROJECT_ROOT, 'templates')))

# in memory list of posts that is loaded at startup
posts = []

def render_template(name, variables):
    """Renders the template ``name`` using ``variables``."""
    template = ENVIRONMENT.get_template(name)
    return template.render(**variables)


class Blog(object):
    def index(self):
        return render_template('index.html', {
            'posts': posts,
        })
    index.exposed = True

# load the posts on startup
post_directory = os.environ['BMBLOG_POST_DIRECTORY']
post_files = [f for f in os.listdir(post_directory)
                if f.endswith('.markdown')]
for f in post_files:
    md = markdown.Markdown(extensions=['meta'])
    html = md.convert(file(os.path.join(post_directory, f)).read())
    posts.append({
        'title': md.Meta['title'][0],
        'date': md.Meta['date'][0],
        'body': html,
    })

cherrypy.quickstart(Blog())
