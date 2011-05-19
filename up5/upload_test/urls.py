from django.conf.urls.defaults import patterns

urlpatterns = patterns('upload_test.views',
        (r'^upload/', 'upload_file'),
)
