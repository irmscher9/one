from app import app
from app.models import User, Post

@app.route('/')
@app.route('/index')
def index():
    return "FSP3!"
