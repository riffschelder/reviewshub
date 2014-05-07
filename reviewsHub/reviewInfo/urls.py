from django.conf.urls import patterns, include, url

import reviewInfo.views

urlpatterns = patterns('',
    url(r'^$', reviewInfo.views.visualize)
)
