from flask import Flask 
from models import db, User
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///school.db'

Migrate = Migrate(app, db)
db.__init__(app)

@app.route('/')
def index():
    return "Hello, World!"
@app.route('/about')
def about():
    return "This is the about page."

@app.route("/<username>")
def username(username):
    return f"hello{username}"

if __name__=='__main__':
 app.run(debug=True,port=4000)
 
 





