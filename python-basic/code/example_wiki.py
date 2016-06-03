from atexit import register
from sqlite3 import connect
from textwrap import dedent
import os
import re

from flask import Flask, g, redirect, request

APP = Flask(__name__)
DBFILE = '/tmp/db.sqlite'
WIKINAME = re.compile(r'\b([A-Z][a-z]+([A-Z0-9][a-z0-9]+)+)\b')


@register
def cleanup():
    try:
        os.unlink(DBFILE)
    except OSError:
        pass


@APP.before_first_request
def bootstrap(*args, **kwargs):
    conn = connect(DBFILE)
    cursor = conn.cursor()
    cursor.execute(dedent(
        '''
        CREATE TABLE page (
            name VARCHAR(64) NOT NULL PRIMARY KEY,
            content TEXT,
            inserted DATETIME NOT NULL DEFAULT NOW,
            updated DATETIME DEFAULT NULL
        );
        '''))
    cursor.execute('INSERT INTO page (name, content) VALUES (?, ?)', (
        'MainPage', 'Hello World! HelloWorld'))
    conn.commit()
    conn.close()


@APP.before_request
def before_request(*args, **kwargs):
    g.db = connect(DBFILE)


@APP.teardown_request
def teardown_request(*args, **kwargs):
    g.db.commit()
    g.db.close()


@APP.route('/')
def index():
    return redirect('/MainPage')


@APP.route('/save', methods=['POST'])
def save_page():
    content = request.form.get('content', '').strip()
    name = request.form.get('pagename', '').strip()
    cursor = g.db.cursor()
    cursor.execute('SELECT COUNT(*) FROM page WHERE name=?', (name, ))
    if cursor.fetchone()[0] == 0:
        cursor.execute('INSERT INTO page (name, content) VALUES (?, ?)', (
            name, content))
    else:
        cursor.execute('UPDATE page SET content=? WHERE name=?', (
            content, name))
    return redirect('/%s' % name)


@APP.route('/<pagename>')
def show_pagename(pagename):
    cur = g.db.cursor()
    cur.execute('SELECT content FROM page WHERE name=?', (pagename, ))
    row = cur.fetchone()
    content = row[0] if row else ''
    if not row or request.args.get('action', 'show') == 'edit':
        # TODO urlencode
        return dedent(
            '''
            <form action="/save" method="POST">
                <input type="hidden" name="pagename" value="%s">
                <textarea name="content" rows="20" cols="80">%s</textarea>
                <br />
                <input type="submit">
            </form>
            ''' % (pagename, content))
    else:
        return '%s<br /><a href="?action=edit">Edit</a>' % (
            WIKINAME.sub(r'<a href="/\1">\1</a>', row[0]), )


if __name__ == '__main__':
    APP.run(port=8080,
            host='0.0.0.0',
            debug=True)
