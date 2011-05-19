ALLDIRS = ['usr/local/pythonenv/PYLONS-1/lib/python2.5/site-packages']

import os
import sys
import site

path = '/var/websites'
if path not in sys.path:
    sys.path.insert(0, '/var/websites')
 
os.environ['DJANGO_SETTINGS_MODULE'] = 'hello.settings'
 
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
