from flask  import *

mod = Blueprint('site', __name__)
@mod.route('/')
def homepage():
    return render_template('/index.html')

