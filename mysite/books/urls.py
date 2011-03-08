from django.conf.urls.defaults import *
import views

urlpatterns = patterns('',
        (r'hello/', views.hello),
        (r'^search_form/$', views.search_form),
        (r'^search/$', views.search),
        (r'^contact/$',views.contact),
        (r'^upload/$', views.upload_file),
)
