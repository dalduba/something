from django.conf.urls import patterns, include, url
from rooms.views import hello, room_details

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', hello),
    url(r'^roomdetails$', room_details),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
