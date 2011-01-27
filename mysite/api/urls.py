from django.conf.urls.defaults import *
from piston.resource import Resource
from mysite.api.handlers import BookHandler

book_handler = Resource(BookHandler)

urlpatterns = patterns('',
        url(r'^book/(?P<book_id>[^/]+)/', book_handler),
        url(r'^books/', book_handler),
    )
