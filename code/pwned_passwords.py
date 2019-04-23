import sys
from getpass import getpass
from hashlib import sha1
from urllib.request import Request, urlopen


def http_get(url):
    '''
    Fetch the contents of *url* using a HTTP GET call
    '''
    # Headers must be set, otherwirse we get a "403 Forbidden" error
    headers = {'User-Agent': 'pythontraining/pwdchecker'}
    request = Request(url, headers=headers, method='GET')

    try:
        response = urlopen(request)
    except Exception as exc:
        print(exc, file=sys.stderr)
        return ''

    if response.code != 200:
        msg = '%d %r' % (response.code, response.read())
        print(msg, file=sys.stderr)
        return ''

    data = response.read()
    return data


def get_password_parts():
    '''
    Prompt the user for a password and return head and tail of the SHA-1 hash.

    Returns the first 5 characters and the remaining characters of the SHA-1
    hash of the password as a tuple
    '''
    try:
        passwd = getpass('Enter your password: ')
    except KeyboardInterrupt:
        return None, None
    passwd = passwd.strip()
    if not passwd:
        return None, None
    hsh = sha1(passwd.encode('utf8')).hexdigest()
    head, tail = hsh[:5], hsh[5:]
    return head, tail


def fetch_group(group):
    '''
    Calls a remote API to fetch all hashes from a given group.
    '''
    url = 'https://api.pwnedpasswords.com/range/' + group
    data = http_get(url)
    text = data.decode('ascii')
    return text


def parse_results(data):
    '''
    Converts the raw document into a dictionary mapping the password hash
    remainder to the number of hits.
    '''
    lines = data.splitlines()
    hits = {}
    for line in lines:
        tmp, _, num_hits = line.partition(':')
        num_hits = int(num_hits)
        hits[tmp] = num_hits
    return hits


def main():
    head, tail = get_password_parts()
    while (head, tail) != (None, None):
        remote_result = fetch_group(head)
        hits_map = parse_results(remote_result)
        hits = hits_map.get(tail.upper(), 0)
        print('Password was hit %d times' % hits)
        head, tail = get_password_parts()


if __name__ == '__main__':
    main()
