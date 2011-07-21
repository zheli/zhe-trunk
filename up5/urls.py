from django.conf.urls.defaults import *
from upload_test.views         import logout, home
from django.contrib            import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hello.views.home', name='home'),
    
    # url(r'^hello/', include('hello.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/',     include(admin.site.urls)),
    url(r'^test/',    include('up5.upload_test.urls')),
    url(r'^logout/$', logout, name='logout'),
    url(r'^$', home, name='home'),
    url(r'', include('social_auth.urls')),
)
