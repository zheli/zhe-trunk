import os

from fabric.api import *
from fabric.contrib.project import rsync_project
from fabric.contrib import files, console
from fabric import utils
from fabric.decorators import hosts
web_service = {}
web_service['ubuntu'] = {
    'apache'    : 'apache2',
    'apachectl' : 'apache2ctl',
}
web_service['centos'] = {
    'apache'    : 'httpd',
    'apachectl' : 'apachectl',
}

RSYNC_EXCLUDE                = (
        '.DS_Store',
        '.hg',
        '*.pyc',
        '*.db',
        'media/admin',
        'media/attachments',
        'media/file',
        'local_settings.py',
        'fabfile.py',
        'bootstrap.py')
env.home                     = '/home/'
env.project                  = 'up5'

def _setup_path():
    env.root            = os.path.join(env.home, env.project, env.environment)
    env.code_root       = os.path.join(env.root, env.project)
    env.virtualenv_root = os.path.join(env.root, 'env')
    env.settings        = '%(project)s.settings_%(environment)s' % env

def staging():
    """ use staging environment on remote host"""
    env.user = 'ec2-user'
    env.environment = 'staging'
    env.hosts = ['67.202.21.91']
    env.web_service = web_service['centos']
    _setup_path()

def production():
    """ use production environment on remote host"""
    utils.abort('Production deployment not yet implemented.')


def bootstrap():
    """ initialize remote host environment (virtualenv, deploy, update) """
    require('root', provided_by=('staging', 'production'))
    run('mkdir -p %(root)s' % env)
    run('mkdir -p %s' % os.path.join(env.home, env.project, 'log'))
    create_virtualenv()
    deploy()
    update_requirements()


def create_virtualenv():
    """ setup virtualenv on remote host """
    require('virtualenv_root', provided_by=('staging', 'production'))
    args = '--clear --distribute'
    run('virtualenv %s %s' % (args, env.virtualenv_root))


def deploy():
    """ rsync code to remote host """
    require('root', provided_by=('staging', 'production'))
    if env.environment == 'production':
        if not console.confirm('Are you sure you want to deploy production?', default=False):
            utils.abort('Production deployment aborted.')
    # defaults rsync options:
    # -pthrvz
    # -p preserve permissions
    # -t preserve times
    # -h output numbers in a human-readable format
    # -r recurse into directories
    # -v increase verbosity
    # -z compress file data during the transfer
    extra_opts = '--omit-dir-times'
    rsync_project(
        env.root,
        exclude=RSYNC_EXCLUDE,
        delete=True,
        extra_opts=extra_opts,
    )
    touch()


def update_requirements():
    """ update external dependencies on remote host """
    require('code_root', provided_by=('staging', 'production'))
    requirements = os.path.join(env.code_root, 'requirements')
    with cd(requirements):
        cmd = ['pip install --upgrade']
        cmd += ['-E %(virtualenv_root)s' % env]
        cmd += ['--requirement %s' % os.path.join(requirements, 'apps.txt')]
        run(' '.join(cmd))


def touch():
    """ touch wsgi file to trigger reload """
    require('code_root', provided_by=('staging', 'production'))
    apache_dir = os.path.join(env.code_root, 'apache')
    with cd(apache_dir):
        run('touch up5_%s.wsgi' % env.environment)


def update_apache_conf():
    """ upload apache configuration to remote host """
    require('code_root', provided_by=('staging', 'production'))
    source = os.path.join(env.code_root, 'apache', '%(project)s_%(environment)s.conf' % env)
    dest = os.path.join(env.home, env.project, 'apache.conf.d')
    #put(source, dest, mode=0755)
    run('ln -sf %s %s' % (os.path.abspath(source), dest))
    apache_reload()


def configtest():    
    """ test Apache configuration """
    require('root', provided_by=('staging', 'production'))
    run('%s configtest' % env.web_service['apachectl'])


def apache_reload():    
    """ reload Apache on remote host """
    require('root', provided_by=('staging', 'production'))
    run('sudo /etc/init.d/%s reload' % env.web_service['apache'])


def apache_restart():    
    """ restart Apache on remote host """
    require('root', provided_by=('staging', 'production'))
    run('sudo /etc/init.d/%s restart' % env.web_service['apache'])


def symlink_django():    
    """ create symbolic link so Apache can serve django admin media """
    require('root', provided_by=('staging', 'production'))
    admin_media = os.path.join(env.virtualenv_root,
            'src/django/django/contrib/admin/media/')
    media = os.path.join(env.code_root, 'media/admin')
    if not files.exists(media):
        run('ln -s %s %s' % (admin_media, media))


def reset_local_media():
    """ Reset local media from remote host """
    require('root', provided_by=('staging', 'production'))
    media = os.path.join(env.code_root, 'media', 'upload')
    local('rsync -rvaz %s@%s:%s media/' % (env.user, env.hosts[0], media))
