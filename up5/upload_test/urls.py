from django.conf.urls.defaults import patterns

urlpatterns = patterns('up5.upload_test.views',
        (r'^upload/'  , 'upload_file'),
        (r'^upload2/' , 'upload_handler'),
        (r'^download/(?P<pk>.+)$', 'download_handler'),
        (r'^delete/(?P<pk>.+)$', 'delete_handler'),
)
