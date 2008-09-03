from django.db import models
from django.db.models import permalink

class Post(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    slug = models.SlugField()
    
    def get_absolute_url(self):
        return ('posts.views.post', [self.slug])
    get_absolute_url = permalink(get_absolute_url)
    
    def __str__(self):
        return self.title
    
    class Admin:
        prepopulated_fields = {'slug':('title',)}
    
    class Meta:
        ordering = ["-date"]
