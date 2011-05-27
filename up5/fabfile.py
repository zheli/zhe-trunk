import os

from fabric.api import *
from fabric.contrib.project import rsync_project
from fabric.contrib import files, console
from fabric import utils
from fabric.decorators import hosts

RSYNC_EXCLUDE = (
        '.DS_Store',
        '.hg',
        '*.pyc',
        '*.db',
        'media/admin',
        'media/attachments',
        'local_settings.py',
        'fabfile.py',
        'bootstrap.py')
env.home = '/home/ec2-user/'
env.prject = 'up5_website'


