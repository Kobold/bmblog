from django.shortcuts import render_to_response
from bmblog.posts.models import Post

def main(request):
    posts = Post.objects.all()
    return render_to_response('main.html', {'posts': posts})
