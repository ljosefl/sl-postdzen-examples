from flask import Flask, request, jsonify
from flask_oauthlib.client import OAuth
import os

app = Flask(__name__)
oauth = OAuth(app)

# Инициализация клиента Okta
okta = oauth.remote_app(
    'okta',
    consumer_key=os.environ.get('OKTA_CLIENT_ID'),
    consumer_secret=os.environ.get('OKTA_CLIENT_SECRET'),
    request_token_params={'scope': 'openid profile email'},
    base_url='https://dev-123456.oktapreview.com/oauth2/default/v1/',
    request_token_url=None,
    access_token_method='POST',
    access_token_url='https://dev-123456.oktapreview.com/oauth2/default/v1/token',
    authorize_url='https://dev-123456.oktapreview.com/oauth2/default/v1/authorize'
)

@app.route('/')
def index():
    return "Welcome to the secure MCP server!"

@app.route('/protected')
@okta.authorized_handler
def protected(resp):
    if resp is None:
        return 'Access denied: reason=%s error=%s' % (
            request.args['error_reason'],
            request.args['error_description']
        )
    session['me'] = resp
    return 'Welcome %s' % resp['email']

@okta.tokengetter
def get_okta_oauth_token():
    return session.get('oauth_token')

if __name__ == '__main__':
    app.run(debug=True)