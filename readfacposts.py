from flask import Flask, redirect, url_for, session, request
from flask_oauth import OAuth

SECRET_KEY = ''
FACEBOOK_APP_ID = ''
FACEBOOK_APP_SECRET = ''
DEBUG = True

app = Flask(__name__)
app.debug = DEBUG
app.secret_key = SECRET_KEY
oauth = OAuth()

facebook = oauth.remote_app('facebook',
    base_url='https://graph.facebook.com/',
    access_token= EAACEdEose0cBAA5N08wDM7DH6S1O5TU3L7pWRCpM8gcABgfYZArD3zkeChVM1Qh838AcvYmoSPwMXXPWLGqtdGmxeoZC4BpTlTcRa8I92IKs0jHvTRoFcvFkfZAlcoxudPOZAvGDafCnZBtkApuoza0e85yl6ZBamD0vrC5QJxqaRM1bSAIINcWm5klONUBbD5w14cSFVL2QZDZD              
    access_token_url='/oauth/access_token',
    authorize_url='https://www.facebook.com/dialog/oauth',
    request_token_params={'scope': 'public_profile,posts'}
    me = facebook.get('/me?fields=id,name,first_name,last_name,age_range,gender,posts')
                            
@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login')
def login():
    return facebook.authorize(callback=url_for('facebook_authorized',
        next=request.args.get('next') or request.referrer or None,
        _external=True))

@app.route('/login/authorized')
@facebook.authorized_handler
def facebook_authorized(resp):
    if resp is None:
        return 'Access denied: reason=%s error=%s' % (
            request.args['error_reason'],
            request.args['error_description']
        )
    session['oauth_token'] = (resp['access_token'], '')
    me = facebook.get('/me')
    return 'type %s, data %s, headers %s, raw_data %s, status %s' % (type(me), str(me.data), str(me.headers), str(me.raw_data), str(me.status))

@facebook.tokengetter
def get_facebook_oauth_token():
    return session.get('oauth_token')

if __name__ == '__main__':
    app.run()
