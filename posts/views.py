from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render_to_response
from feeds import PostsFeed
from models import Post

def main(request):
    posts = Post.objects.all()
    return render_to_response('main.html', {'posts': posts})

def post(request, slug):
    try:
        return render_to_response('post.html',
            {'post': Post.objects.get(slug=slug)})
    except Post.DoesNotExist:
        return HttpResponseNotFound()

def feed(request):
    feedgen = PostsFeed('', request).get_feed('')
    response = HttpResponse(mimetype=feedgen.mime_type)
    feedgen.write(response, 'utf-8')
    return response
