# -*- coding: utf-8 -*-
from jinja2 import Environment, FileSystemLoader
import cherrypy
import os

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
ENVIRONMENT = Environment(
    loader=FileSystemLoader(os.path.join(PROJECT_ROOT, 'templates')))


def render_template(name, variables):
    """Renders the template ``name`` using ``variables``."""
    template = ENVIRONMENT.get_template(name)
    return template.render(**variables)


class Blog(object):
    def index(self):
        return render_template('index.html', {
            'phrase': "Hello world!",
        })
    index.exposed = True

cherrypy.quickstart(Blog())
