from os import environ
from os.path import abspath

from fabric.connection import Connection
from invoke import task

www = Connection('michel.albert.lu')

INSTANCE = '2018'
VIRTUAL_ENV = abspath('./env')
ENVPATH = '%s/bin:%s' % (VIRTUAL_ENV, environ['PATH'])
CUSTOM_ENV = {'PATH': ENVPATH, 'VIRTUAL_ENV': VIRTUAL_ENV}


@task
def fetch_common_files(ctx):
    '''
    Put shared files from the "common" folder of the repository into the proper
    place for building.
    '''
    ctx.run('cp -v common/custom.css slides/_static')


@task
def build_slides(ctx):
    fetch_common_files(ctx)
    ctx.run('cp -v common/slidestyle.css slides/_static/htmlstyle.css')
    with ctx.cd('slides'):
        ctx.run('make slides', env=CUSTOM_ENV)


@task
def build_html(ctx):
    fetch_common_files(ctx)
    ctx.run('cp -v common/htmlstyle.css slides/_static/htmlstyle.css')
    with ctx.cd('slides'):
        ctx.run('export', env=CUSTOM_ENV)
        ctx.run('make html', env=CUSTOM_ENV)


@task
def build_linked(ctx):
    fetch_common_files(ctx)
    with ctx.cd('slides'):
        ctx.run('make slides html', env=CUSTOM_ENV)


@task
def develop(ctx):
    ctx.run('[ -d env ] || python3 -m venv env', env=CUSTOM_ENV)
    ctx.run('./env/bin/pip install hieroglyph', env=CUSTOM_ENV)
    ctx.run('git submodule init', env=CUSTOM_ENV)
    ctx.run('git submodule update', env=CUSTOM_ENV)


@task
def clean(ctx):
    with ctx.cd('slides'):
        ctx.run('/usr/bin/make clean', env=CUSTOM_ENV)


@task
def serve_slides(ctx):
    clean(ctx)
    build_slides(ctx)
    with ctx.cd('slides/_build/slides'):
        ctx.run('python3 -m http.server')


@task
def serve_html(ctx):
    clean(ctx)
    build_html(ctx)
    with ctx.cd('slides/_build/html'):
        ctx.run('python3 -m http.server')


@task
def serve_linked(ctx):
    clean(ctx)
    build_linked(ctx)
    with ctx.cd('slides/_build'):
        ctx.run('python3 -m http.server')


@task
def publish(ctx):
    remote_root = '/var/www/html/shelf'
    remote_folder = '%s/python-basic-%s' % (remote_root, INSTANCE)
    latest_folder = '%s/python-basic-latest' % remote_root
    build_html(ctx)
    build_slides(ctx)
    www.run('mkdir -p %s' % remote_folder)
    www.put('slides/_build/html', remote_folder)
    www.put('slides/_build/slides', remote_folder)
    try:
        www.run('test -h {0} && rm {0}'.format(latest_folder))
    except Exception as exc:
        print(exc)
    www.run('ln -s %s %s' % (remote_folder, latest_folder))

    pack_folder = 'python-basic-%s' % INSTANCE
    ctx.run('mkdir -p %s' % pack_folder)
    ctx.run('mv slides/_build/html slides/_build/slides %s' % pack_folder)
    ctx.run('tar czf %s.tar.gz %s' % (pack_folder, pack_folder))
    ctx.run('rm -rf %s' % pack_folder)
    www.put('%s.tar.gz' % pack_folder, remote_folder)


@task
def autobuild(ctx):
    '''
    Monitor files for changes and automacally build
    '''
    ctx.run('find slides common -name "*.rst" -or -name "*.css" | '
            'entr -c sh -c "fab build-linked"',
            replace_env=False)
