from django.conf.urls.defaults import *
import upload

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     (r'^admin/',   include(admin.site.urls)),
     (r'api/',      include('mysite.api.urls')),
     (r'upload/',   'upload.views.upload_handler'),
     (r'^download/(?P<pk>.+)$', 'upload.views.download_handler'),
     (r'',        include('books.urls')),
)
