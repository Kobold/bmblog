from fabric.api import *
from fabric.contrib.project import rsync_project

env.hosts = ['andrewkish.name']
env.user = 'andrewkish'

def deploy():
    """Deploys the latest version of the code to the server."""
    local('python blog.py')
    rsync_project(local_dir='output/', remote_dir='~/public_html')
