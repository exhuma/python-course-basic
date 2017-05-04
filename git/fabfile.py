import fabric.api as fab

fab.env.roledefs['www'] = ['exhuma@michel.albert.lu']
INSTANCE = '2016'


@fab.task
def build_slides():
    fab.local('make slides')


@fab.task
def build_html():
    fab.local('make html')


@fab.task
def build_linked():
    fab.local('make slides html')


@fab.task
def clean():
    fab.local('make clean')


@fab.task
def serve_slides():
    fab.execute(clean)
    fab.execute(build_slides)
    with fab.lcd('_build/slides'):
        fab.local('python3 -m http.server')


@fab.task
def serve_html():
    fab.execute(clean)
    fab.execute(build_html)
    with fab.lcd('_build/html'):
        fab.local('python3 -m http.server')


@fab.task
def serve_linked():
    fab.execute(clean)
    fab.execute(build_linked)
    with fab.lcd('_build'):
        fab.local('python3 -m http.server')


@fab.task
@fab.roles('www')
def publish():
    remote_folder = '/var/www/albert.lu/michel/shelf/git-%s' % INSTANCE
    latest_folder = '/var/www/albert.lu/michel/shelf/git-latest'
    fab.execute(build_linked)
    fab.run('mkdir -p %s' % remote_folder)
    fab.put('_build/html', remote_folder)
    fab.put('_build/slides', remote_folder)
    with fab.settings(warn_only=True):
        fab.run('test -h {0} && rm {0}'.format(latest_folder))
    fab.run('ln -s %s %s' % (remote_folder, latest_folder))


@fab.task
def run_gitlab():
    with fab.lcd('gitlab'):
        fab.local('GITLAB_SECRETS_DB_KEY_BASE=fo43287r4y398fhuo4837fy3894f '
                  'docker-compose up')
