from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("<html><body>Hello world.</body></html>")
