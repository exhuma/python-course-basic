from os.path import exists
from sqlite3 import connect

DBFILE = '/tmp/db.sqlite'


def create_database(connection):
    '''
    Creates the database.

    :param connection: A database connection.
    '''
    if exists(DBFILE):
        return
    cursor = connection.cursor()
    cursor.execute(
        '''
        CREATE TABLE page (
            name VARCHAR(64) NOT NULL PRIMARY KEY,
            content TEXT,
            inserted DATETIME NOT NULL DEFAULT NOW,
            updated DATETIME DEFAULT NULL
        );
        ''')
    cursor.execute('INSERT INTO page (name, content) VALUES (?, ?)', (
        'MainPage', 'Hello World! HelloWorld'))
    connection.commit()


def add_page(connection, name, content):
    '''
    Inserts or updates a page in the database.
    '''
    cursor = connection.cursor()
    cursor.execute('SELECT COUNT(*) FROM page WHERE name=?', (name, ))
    if cursor.fetchone()[0] == 0:
        cursor.execute('INSERT INTO page (name, content) VALUES (?, ?)', (
            name, content))
    else:
        cursor.execute('UPDATE page SET content=? WHERE name=?', (
            content, name))


def retrieve(connection, pagename):
    cursor = connection.cursor()
    cursor.execute('SELECT content FROM page WHERE name=?', (pagename, ))
    row = cursor.fetchone()
    content = row[0] if row else ''
    return content


if __name__ == '__main__':
    conn = connect(DBFILE)
    add_page(conn,
             'helloworld',
             'This is a sample pgage')
    content = retrieve(conn, 'helloworld')
    print('The content of "Hello World" is: %r' % content)
    conn.close()
