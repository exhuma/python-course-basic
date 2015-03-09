from flask import Flask


APP = Flask(__name__)


@APP.route('/')
def index():
    return 'Hello World'


if __name__ == '__main__':
    APP.run(port=8080,
            host='0.0.0.0',
            debug=True)
