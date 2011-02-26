from django.conf.urls.defaults import *
from views import hello

urlpatterns = patterns('',
        (r'hello/', hello),
)
