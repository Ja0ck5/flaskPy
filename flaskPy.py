from flask import Flask

app = Flask(__name__)


# @app.route('/')
@app.route('/index/<user>', methods=['POST', 'GET'])
def hello_world(user):
    # aint = 1
    # astr = '1'
    # result =  aint + astr
    # return 'Hello World!'
    return 'Hello %s' % user


if __name__ == '__main__':
    app.run(debug=True)
