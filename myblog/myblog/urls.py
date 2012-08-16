from django.conf.urls.defaults import *
from django.contrib import admin
import settings
# Uncomment the next two lines to enable the admin:
admin.autodiscover()
from weblog.feeds import CategoryFeed, LatestEntriesFeed

feeds = {'entries':LatestEntriesFeed,
	 'categories':CategoryFeed }


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myblog.views.home', name='home'),
    # url(r'^myblog/', include('myblog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)), 
    (r'^tiny_mce/(?P<path>.*)$', 'django.views.static.serve',
	    {'document_root':'/Users/Mars/Desktop/PythonDev/projects/djcode/tinymce/jscripts/tiny_mce'}),
    (r'^search/$', 'search.views.search'),
    (r'^comments/', include('django.contrib.comments.urls')),
    (r'^weblog/categories/', include('weblog.urls.categories')),
    (r'^weblog/links/', include('weblog.urls.links')),
    (r'^weblog/tags/', include('weblog.urls.tags')),
    (r'^weblog/', include('weblog.urls.entries')),
    (r'^weblog/feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.Feed', { 'feed_dict': feeds }),
    (r'^codeshare/', include('cab.urls.home')),
    (r'^codeshare/snippets/', include('cab.urls.snippets')),
    (r'^codeshare/languages/', include('cab.urls.languages')),
    (r'^codeshare/popular/', include('cab.urls.popular')),
    (r'^codeshare/tags/', include('cab.urls.tags')),
    (r'^codeshare/bookmarks/', include('cab.urls.bookmarks')),
    (r'^codeshare/ratings/', include('cab.urls.ratings')),
    (r'^codeshare/css/(?P<path>.*)$', 'django.views.static.serve', 
	    { 'document_root':'/Users/Mars/Desktop/PythonDev/projects/djcode/myblog/cab/css/' }),
    (r'', include('django.contrib.flatpages.urls')),

)
