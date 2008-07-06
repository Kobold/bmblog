from django.contrib.syndication.feeds import Feed
from django.utils.feedgenerator import Atom1Feed
from models import Post

class PostsFeed(Feed):
    '''Feed for latest 15 blog entries'''
    
    title = 'Booze and Mescaline'
    link = 'http://boozeandmescaline.com' #URI of site
    subtitle = 'Most recent posts'
    feed_type = Atom1Feed
    
    title_template = 'feed_title.html'
    description_template = 'feed_description.html'

    def items(self):
        return Post.objects.order_by('-date')[:15]
    
    def item_pubdate(self, item):
        return item.date
