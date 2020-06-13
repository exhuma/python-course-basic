from os import environ
from os.path import abspath

from fabric.connection import Connection
from invoke import task
from patchwork.transfers import rsync as rsync_

www = Connection('ec2-user@michel.albert.lu')

INSTANCE = '2020'
VIRTUAL_ENV = abspath('./env')
ENVPATH = '%s/bin:%s' % (VIRTUAL_ENV, environ['PATH'])
CUSTOM_ENV = {'PATH': ENVPATH, 'VIRTUAL_ENV': VIRTUAL_ENV}


def rsync(ctx, *args, **kwargs):  # type: ignore
    """Ugly workaround for https://github.com/fabric/patchwork/issues/16."""
    ssh_agent = environ.get('SSH_AUTH_SOCK', None)
    if ssh_agent:
        ctx.config['run']['env']['SSH_AUTH_SOCK'] = ssh_agent
    return rsync_(ctx, *args, **kwargs)


@task
def publish(ctx):
    remote_root = '/var/www/html/shelf'
    remote_folder = '%s/python-basic-%s' % (remote_root, INSTANCE)
    latest_folder = '%s/python-basic-latest' % remote_root
    www.run('mkdir -p %s' % remote_folder)
    rsync(www, 'reveal.js', remote_folder, delete=True, exclude=[
        "node_modules",
    ])
    try:
        www.run('test -h {0} && rm {0}'.format(latest_folder))
    except Exception as exc:
        print(exc)
    www.run('ln -s %s %s' % (remote_folder, latest_folder))

    pack_folder = 'python-basic-%s' % INSTANCE
    ctx.run('mkdir -p %s' % pack_folder)
    ctx.run('cp -r reveal.js %s' % pack_folder)
    ctx.run('rm -rf %s/reveal.js/node_modules' % pack_folder)
    ctx.run('tar czf %s.tar.gz %s' % (pack_folder, pack_folder))
    ctx.run('rm -rf %s' % pack_folder)
    www.put('%s.tar.gz' % pack_folder, remote_folder)
    ctx.run('rm -f %s.tar.gz' % pack_folder)
