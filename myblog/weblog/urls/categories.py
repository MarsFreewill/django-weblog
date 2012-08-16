from django.conf.urls.defaults import *
from weblog.models import Category

urlpatterns = patterns('',
                       (r'^$', 'django.views.generic.list_detail.object_list',
                        {'queryset':Category.objects.all() }, 'weblog_category_list'),
                       (r'^(?P<slug>[-\w]+)/$', 'weblog.views.category_detail', {}, 'weblog_category_detail'),
                       )
