import base64
import random
import time

from flask import Flask, request, redirect

app = Flask(__name__)

users = {
    'name': ['123456']
}


def get_token(uid):
    token = base64.b64encode(':'.join([str(uid), str(random.random()), str(time.time() + 7200)]))
    users[uid].append(token)
    return token


def verify_token(token):
    _token = base64.b64decode(token)
    if not users.get(_token.split(':')[0])[-1] == token:
        return -1
    if float(_token.split(':')[-1]) >= time.time():
        return 1
    else:
        return 0


# @app.route('/')
@app.route('/index/<user>', methods=['POST', 'GET'])
def hello_world(user):
    # aint = 1
    # astr = '1'
    # result =  aint + astr
    # return 'Hello World!'
    print request.headers
    return 'Hello %s' % user


@app.route('/login', methods=['POST', 'GET'])
def login():
    uid, pw = base64.b64decode(request.headers['Authorization'].split(' ')[-1]).split(':')
    if users.get(uid)[0] == pw:
        return get_token(uid)
    else:
        return 'error'


@app.route('/test', methods=['POST', 'GET'])
def test():
    token = request.args.get('token')
    if 1 == verify_token(token):
        return 'OK'
    else:
        return 'error'

@app.route('/client/login', methods=['POST', 'GET'])
def client_login():
   uri = 'http://127.0.0.1:5000/oauth'
   return redirect(uri)

@app.route('/oauth', methods=['POST', 'GET'])
def oauth():
   return 'test oauth'

if __name__ == '__main__':
    app.run(debug=True)
