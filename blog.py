# -*- coding: utf-8 -*-
from jinja2 import Environment, FileSystemLoader
import dateutil.parser
import markdown
import operator
import os
import shutil


PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
TEMPLATE_ROOT = os.path.join(PROJECT_ROOT, 'templates')
POST_DIRECTORY = os.path.join(PROJECT_ROOT, 'posts')
STATIC_DIRECTORY = os.path.join(PROJECT_ROOT, 'static')
OUTPUT_DIRECTORY = os.path.join(PROJECT_ROOT, 'output')


environment = Environment(loader=FileSystemLoader(TEMPLATE_ROOT))


def date(value, format='%B %e, %Y'):
    """Nice formatting for datetime strings."""
    return value.strftime(format)
environment.filters['date'] = date


def url(item):
    return u'/%s/%s/' % (item['type'], item['slug'])
environment.filters['url'] = url


def parse_files():
    md_files = [f for f in os.listdir(POST_DIRECTORY)
                if f.endswith('.markdown')]
    
    posts, pages = [], []
    for f in md_files:
        md = markdown.Markdown(extensions=['meta'])
        text = file(os.path.join(POST_DIRECTORY, f)).read().decode('utf-8')
        html = md.convert(text)
        
        type = md.Meta['type'][0]
        md_dict = {
            'title': md.Meta['title'][0],
            'slug': f[:-9], # slice off the .markdown to create the slug
            'body': html,
            'type': type,
        }
        if type == 'post':
            md_dict.update({'date': dateutil.parser.parse(md.Meta['date'][0])})
            posts.append(md_dict)
        elif type == 'page':
            pages.append(md_dict)
    
    return posts, pages


if __name__ == '__main__':
    if os.path.exists(OUTPUT_DIRECTORY):
        shutil.rmtree(OUTPUT_DIRECTORY)
    
    os.mkdir(OUTPUT_DIRECTORY)
    shutil.copytree(STATIC_DIRECTORY, os.path.join(OUTPUT_DIRECTORY, 'static'))
    
    posts, pages = parse_files()
    with file(os.path.join(OUTPUT_DIRECTORY, 'index.html'), 'w') as f:
        posts = sorted(posts, key=operator.itemgetter('date'), reverse=True)
        template = environment.get_template('index.html')
        f.write(template.render(item=posts[0], older_posts=posts[1:],
                                pages=pages).encode('utf-8'))
    
    os.mkdir(os.path.join(OUTPUT_DIRECTORY, 'page'))
    os.mkdir(os.path.join(OUTPUT_DIRECTORY, 'post'))
    for p in pages + posts:
        filename = os.path.join(OUTPUT_DIRECTORY, p['type'], p['slug'] + '.html')
        with file(filename, 'w') as f:
            template = environment.get_template('post.html')
            f.write(template.render(item=p, pages=pages).encode('utf-8'))

