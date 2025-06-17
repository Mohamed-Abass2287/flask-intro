from flask import Flask, make_response, request
from flask_migrate import Migrate
from models import db, User, Post
from blueprints.posts import post_pb
from blueprints.users import user_bp
from flask_restful import Api, Resource

# create the app
app = Flask(__name__)

# configure the SQLite database, relative to the app instance folder
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///school.db'

migrate = Migrate(app, db)

# initialize the app with the extension
db.init_app(app)
api = Api(app)


# # registering blueprint
# app.register_blueprint(user_bp, url_prefix='/api/v1')
# app.register_blueprint(post_pb, url_prefix='/api/v1')


# @app.route('/')
# def index():
#     return "Hello World!"

# @app.route('/about')
# def about():
#     return "This is about us page"

# @app.route("/<username>")
# def username(username):
#     return f'Hello {username}'


#CLASS BASED ENDPOINTS
class postEndpoint(Resource):
    def get(self):
        posts = [post.to_dict() for post in Post.query.all()]
        return make_response({'posts': posts}, 200)
    
    def post(self):
        data = request.get_json()
        new_post = Post(title=data['post_title'], content=data['post_content'], user_id=data['user_id'])
        db.session.add(new_post)
        db.session.commit()
        return make_response({'post': new_post.to_dict()}, 201)
    
class postEndpointByid(Resource):
    def get(self, post_id):
       post = db.get_or_404(Post, post_id)
       return make_response({'post': post.to_dict()}, 200)
    
    def patch(self, post_id):
        post = db.get_or_404(Post, post_id)
        data = request.get_json()
        
        for key, value in data.items():
            setattr(post, key, value)
        db.session.commit()
        return make_response({'post': post.to_dict()}, 200)

    def delete(self, post_id):
        post = db.get_or_404(Post, post_id)
        db.session.delete(post)
        db.session.commit()
        return make_response({'message': 'Post deleted successfully'}, 204)


api.add_resource(postEndpoint, '/posts')
api.add_resource(postEndpointByid, '/posts/<int:post_id>')




if __name__ == '__main__':
    app.run(debug=True, port=5000)

















