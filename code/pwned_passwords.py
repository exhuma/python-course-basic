"""
This appllication prompts the user for a password and verifies if this password
has ever been subject to a leak. The application uses the API from
api.pwnedpasswords.com
"""
import sys
from getpass import getpass
from hashlib import sha1
from urllib.request import Request, urlopen


def http_get(url):
    """
    Fetch the contents of *url* using a HTTP GET call
    """
    # Headers must be set, otherwirse we get a "403 Forbidden" error
    headers = {'User-Agent': 'pythontraining/pwdchecker'}
    request = Request(url, headers=headers, method='GET')

    try:
        response = urlopen(request)
    except Exception as exc:
        # Somethin unexpected happened. We will print out the error message.
        # But instead of writing it to the "standard output stream" we write it
        # into the "standard error stream". Note that the value given to
        # "file=" can also be an opened file object
        print(exc, file=sys.stderr)
        # After showing the erro to the user we return a "default" value: An
        # empty "bytes" object
        return b''

    # We check the "code" of the response. In HTTP the 200 code means that
    # everything is OK. If it is anything else the API did not return what we
    # expected. Normally a response will also contain a text explaining what
    # went wrong. We show this to the user and return a default empty-bytes
    # object again
    if response.code != 200:
        msg = '%d %r' % (response.code, response.read())
        print(msg, file=sys.stderr)
        return b''

    # If we reached this point (if we have not "returned from the function yet)
    # we should have no error (code was 200 and we had no exception). We can
    # read the data and return it from the function
    data = response.read()
    return data


def get_password_parts():
    """
    Prompt the user for a password and return the first 5 characters and the
    following, remaining characters as two separate values.
    """
    try:
        passwd = getpass('Enter your password: ')
    except KeyboardInterrupt:
        # The "KeyboardInterrupt" is a special exception which is thrown/raised
        # when the user presses "CTRL-C" on the keyboard. We catch this and
        # return default values.
        # This meand the user can press CTRL-C during the password prompt and
        # the application will *not* exit but cause this function to return
        # empty values. They must then be handled later on.
        return None, None

    # Remove any junk whitespace from user-input. This is generally a good
    # idea.
    passwd = passwd.strip()

    # Next, we may end up with an empty string. We cannot "split" empty strings
    # and need to decide what to do with that. Here, I decided to return the
    # default empty values.
    if not passwd:
        return None, None

    # Now we can convert the password to a hexadecimal representation of a
    # SHA-1 hash., split it into the two parts and return the values.
    encoded_password = passwd.encode('utf8')
    hsh = sha1(encoded_password).hexdigest()
    head, tail = hsh[:5], hsh[5:]
    return head, tail


def fetch_group(group):
    """
    Calls a remote API to fetch all hashes from a given group.
    """
    # Make the HTTP call to fetch the data
    url = 'https://api.pwnedpasswords.com/range/' + group
    data = http_get(url)
    # The data will be returnedas bytes and we need to decode it. It is up to
    # the you, the developer to make sure that you use the correct encoding.
    # This is either documented fo the "content-type" of the HTTP response (for
    # example "application/json" is always UTF-8. If it is not possible to
    # determine it from the content-type, it should be documented on the API.
    text = data.decode('ascii')
    return text


def parse_results(data):
    """
    Converts the raw document from the HTTP response into a dictionary mapping
    the password hash remainder to the number of hits.
    """
    lines = data.splitlines()

    # In this exampe we will load all the results and put them into a
    # dictionary for lookup. This is a bit of overkill. Using a dictionary
    # servers as an exercise for dictionaries.
    hits = {}
    for line in lines:
        # The "partition" function on strings is very similar to "split", but
        # it will always return exectly 3 values. The part before the first
        # occurrence of the separator, the separator and the remaining part.
        # In Python, by convention the variable "_" can be used for values that
        # you want to ignore.
        tmp, _, num_hits = line.partition(':')
        num_hits = int(num_hits)
        hits[tmp] = num_hits
    return hits


def main():
    """
    The main function of the application
    """
    # Ask the user for a password and split the value.
    head, tail = get_password_parts()

    # If the return of this function was "None, None" we can stop.
    while (head, tail) != (None, None):
        remote_result = fetch_group(head)
        hits_map = parse_results(remote_result)

        # The function "get" on dicitonaries allows us to specify a default
        # value (in this case: 0) which will be returned if the key does not
        # exist in the dictionary.
        hits = hits_map.get(tail.upper(), 0)
        print('Password was hit %d times' % hits)

        # Ask the user one-more time for a password to continue the loop
        head, tail = get_password_parts()


# This "if" line, is not strictly necessary, but it is good programming
# practice for console scripts.
if __name__ == '__main__':
    main()
