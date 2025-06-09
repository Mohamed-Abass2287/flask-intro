from flask import Flask 
app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"
@app.route('/about')
def about():
    return "This is the about page."

@app.route("/<username>")
def username(usename):
    return f"hello{username}"

if __name__=='__main__':
 app.run(debug=True,port=4000)
 





