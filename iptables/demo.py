#!/usr/bin/env python
import flask, flask.views
from os import *
import functools
import base64
import socket

app = flask.Flask(__name__)
app.secret_key = "232431250303"



def is_valid_ipv4_address(address):
    try:
        socket.inet_pton(socket.AF_INET, address)
    except AttributeError:  
        try:
            socket.inet_aton(address)
        except socket.error:
            return False
        return address.count('.') == 3
    except socket.error:  
        return False

    return True

class Main(flask.views.MethodView):
    def get(self):
        return flask.render_template('index.html')
    
    def post(self):
        if 'logout' in flask.request.form:
            flask.session.pop('username', None)
            return flask.redirect(flask.url_for('index'))
        required = ['username', 'passwd']
        for r in required:
            if r not in flask.request.form:
                flask.flash("Error: {0} is required.".format(r))
                return flask.redirect(flask.url_for('index'))
        username = flask.request.form['username']
        passwd = flask.request.form['passwd']
	comp = popen("cat passwd.pass", "r").read()
        if username == "root" and base64.b64decode(comp[:(len(comp)-1)]) == passwd:
            flask.session['username'] = username
        else:
            flask.flash("Username doesn't exist or incorrect password")
        return flask.redirect(flask.url_for('index'))


def login_required(method):
    @functools.wraps(method)
    def wrapper(*args, **kwargs):
        if 'username' in flask.session:
            return method(*args, **kwargs)
        else:
            flask.flash("A login is required to see the page!")
            return flask.redirect(flask.url_for('index'))
    return wrapper


class change(flask.views.MethodView):
    @login_required
    def get(self):       
	return flask.render_template('change.html')

    @login_required
    def post(self):
        old_pass   = flask.request.form['username']
        passwd     = flask.request.form['password']
	compd = popen("cat passwd.pass", "r").read()
	passm = base64.b64decode(compd[:(len(compd)-1)])
	if old_pass == 	passm:
		passwdk = base64.b64encode(passwd)
		system("echo "+passwdk+" > passwd.pass")

		return flask.redirect(flask.url_for('remote'))
	else:
		return flask.redirect(flask.url_for('change'))

	
class Remote(flask.views.MethodView):
    @login_required
    def get(self):
        return flask.render_template('remote.html')
        
    @login_required
    def post(self):
	if is_valid_ipv4_address(flask.request.form['enable']):
		data = flask.request.form['enable']
		vdata = "popen('./script.py  "	
		vdata = vdata + data
		vdata = vdata + " enable', 'r').read()"
		result = eval(vdata)        
		flask.flash(result)
		return flask.redirect(flask.url_for('remote'))
	elif is_valid_ipv4_address(flask.request.form['disable']):
		data = flask.request.form['disable']
		vdata = "popen('./script.py  "	
		vdata = vdata + data
		vdata = vdata + " disable', 'r').read()"
		result = eval(vdata)        
		flask.flash(result)
		return flask.redirect(flask.url_for('remote'))
	else:
		vdata = "popen('./script.py  list', 'r').read()"
		result = eval(vdata)
		flask.flash(result)
		return flask.redirect(flask.url_for('remote'))

class block(flask.views.MethodView):
    @login_required
    def get(self):
        return flask.render_template('block.html')
        
    @login_required
    def post(self):
	if is_valid_ipv4_address(flask.request.form['enable']):
		data = flask.request.form['enable']
		vdata = "popen('./script2.py  "	
		vdata = vdata + data
		vdata = vdata + " block', 'r').read()"
		result = eval(vdata)        
		flask.flash(result)
		return flask.redirect(flask.url_for('block'))
	elif is_valid_ipv4_address(flask.request.form['disable']):
		data = flask.request.form['disable']
		vdata = "popen('./script2.py  "	
		vdata = vdata + data
		vdata = vdata + " unblock', 'r').read()"
		result = eval(vdata)        
		flask.flash(result)
		return flask.redirect(flask.url_for('block'))
	else:
		vdata = "popen('./script2.py  list', 'r').read()"
		result = eval(vdata)
		flask.flash(result)
		return flask.redirect(flask.url_for('block'))

	

app.add_url_rule('/block/',
                 view_func=block.as_view('block'),
                 methods=['GET', 'POST'])    

app.add_url_rule('/',
                 view_func=Main.as_view('index'),
                 methods=["GET", "POST"])


app.add_url_rule('/remote/',
                 view_func=Remote.as_view('remote'),
                 methods=['GET', 'POST'])



app.add_url_rule('/change/',
                 view_func=change.as_view('change'),
                 methods=['GET', 'POST'])





app.run(host='localhost', port=int(8080), debug=True)
