from flask  import *
mod = Blueprint('api', __name__)
@mod.route('/getstuff')
def getstuff():
    return '{"result" : " You are in the API !! "}'




