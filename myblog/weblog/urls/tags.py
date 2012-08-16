from django.conf.urls.defaults import *
from weblog.models import Entry, Link
from tagging.models import Tag

urlpatterns = patterns('',
                       (r'^$', 'django.views.generic.list_detail.object_list',
                        { 'queryset': Tag.objects.all(),
                          'template_name':'weblog/tag_list.html'},
                          'weblog_tag_list'),
                       (r'^entries/(?P<tag>[-\w]+)/$',
                        'tagging.views.tagged_object_list',
                        { 'queryset_or_model': Entry.live.all(),
                          'template_name': 'weblog/entries_by_tag.html' },
                          'weblog_entry_archive_tag'),
                       (r'^links/(?P<tag>[-\w]+)/$',
                        'tagging.views.tagged_object_list',
                        { 'queryset_or_model': Link.objects.all(),
                          'template_name': 'weblog/links_by_tag.html' },
                          'weblog_link_archive_tag'),
                       )
