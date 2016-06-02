'''
In this file
------------

* Classes
* Named parameters
* Defaul Parameters
'''


from os.path import exists
from sqlite3 import connect


class DocumentStore(object):

    def __init__(self, connection=None):  # Default parameter, "constructor"
        self.__default_filename = '/tmp/db.sqlite'
        if not connection:
            self.connection = connect(self.__default_filename)
        else:
            self.connection = connection

    def create_database(self):
        '''
        Creates the database.
        '''
        if exists(self.__default_filename):
            return
        cursor = self.connection.cursor()
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
        self.connection.commit()

    def put(self, name, content):
        '''
        Inserts or updates a page in the database.
        '''
        cursor = self.connection.cursor()
        cursor.execute('SELECT COUNT(*) FROM page WHERE name=?', (name, ))
        if cursor.fetchone()[0] == 0:
            cursor.execute('INSERT INTO page (name, content) VALUES (?, ?)', (
                name, content))
        else:
            cursor.execute('UPDATE page SET content=? WHERE name=?', (
                content, name))

    def get(self, pagename):
        cursor = self.connection.cursor()
        cursor.execute('SELECT content FROM page WHERE name=?', (pagename, ))
        row = cursor.fetchone()
        content = row[0] if row else ''
        return content


if __name__ == '__main__':
    conn = connect('/tmp/myfile.sqlite')
    app = DocumentStore(connection=conn)  # Named parameter, Instantiation
    app.put('helloworld', 'This is a sample page')
    content = app.get('helloworld')
    print('The content of "Hello World" is: %r' % content)
    conn.close()
