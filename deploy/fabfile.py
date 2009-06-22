from fabric.api import *

env.hosts = ['boozeandmescaline.com']
env.user = 'admin'

def deploy():
    """Deploys the latest version of the code to the server."""
    run('cd domains/boozeandmescaline.com/bmblog2 && git pull')
    run('cd domains/boozeandmescaline.com/bmblog2-virtualenv && '
        'pip install -E . -r ~/domains/boozeandmescaline.com/bmblog2/requirements.txt')
    restart_apache()

def deploy_posts():
    """Pulls the latest posts down to the server."""
    run('cd domains/boozeandmescaline.com/bmblog2 && git pull')
    restart_apache()

def restart_apache():
    sudo('apachectl restart')
