import site

from flask import Flask
from blue import api
from login import app
app = Flask(__name__)

from blue.api.routes import mod
from blue.site.routes import  mod
from blue.login.app import app



app.register_blueprint(site.routes.mod)
app.register_blueprint(api.routes.mod, url_prefix='/api')
app.register_blueprint(login.app.app, url_prefix='/login')


