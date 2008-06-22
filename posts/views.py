from django.http import HttpResponseNotFound
from django.shortcuts import render_to_response
from bmblog.posts.models import Post

def main(request):
    posts = Post.objects.all()
    return render_to_response('main.html', {'posts': posts})

def post(request, slug):
    try:
        return render_to_response('post.html',
            {'post': Post.objects.get(slug=slug)})
    except Post.DoesNotExist:
        return HttpResponseNotFound()
