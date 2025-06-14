from flask import Flask, make_response, request
from flask_migrate import Migrate
from models import db, User, Post
from blueprints.posts import post_pb
from blueprints.users import user_bp

# create the app
app = Flask(__name__)

# configure the SQLite database, relative to the app instance folder
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///school.db'

migrate = Migrate(app, db)

# initialize the app with the extension
db.init_app(app)

# registering blueprint
app.register_blueprint(user_bp, url_prefix='/api/v1')
app.register_blueprint(post_pb, url_prefix='/api/v1')


@app.route('/')
def index():
    return "Hello World!"

@app.route('/about')
def about():
    return "This is about us page"

@app.route("/<username>")
def username(username):
    return f'Hello {username}'




    
if __name__ == '__main__':
    app.run(debug=True, port=4000)



















