import fabric.api as fab

fab.env.roledefs['www'] = ['exhuma@michel.albert.lu']


@fab.task
def build_slides():
    with fab.lcd('slides'):
        fab.local('make slides')


@fab.task
def build_html():
    with fab.lcd('slides'):
        fab.local('make html')


@fab.task
def clean():
    with fab.lcd('slides'):
        fab.local('make clean')


@fab.task
@fab.roles('www')
def publish():
    fab.execute(build_html)
    fab.execute(build_slides)
    fab.put('slides/_build/html',
            '/var/www/albert.lu/michel/shelf/python2015')
    fab.put('slides/_build/slides',
            '/var/www/albert.lu/michel/shelf/python2015')
