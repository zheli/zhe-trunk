from django.conf.urls.defaults import *

urlpatterns = patterns('',
        url(r'upload/', 'upload.views.upload_handler'),
        )

