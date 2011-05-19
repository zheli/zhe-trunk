from django.conf.urls.defaults import *
from piston.resource import Resource
from mysite.api.handlers import BookHandler, AuthorHandler

book_handler = Resource(BookHandler)
author_handler = Resource(AuthorHandler)

urlpatterns = patterns('',
        url(r'^book/(?P<book_id>[^/]+)/', book_handler),
        url(r'^books/', book_handler),
        url(r'^author/', author_handler),
    )
