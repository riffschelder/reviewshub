from django.conf.urls import patterns, url

import search.views

urlpatterns = patterns('',
    url(r'^$', search.views.search, name='search_index'),
)