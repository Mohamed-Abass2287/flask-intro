# flask-intro
insert => adding new record update delete select => SELECT * FROM database_name

all = []

all => to get all records filter filter_by delete order_by get update add

sesssion add => adding new record commit => to save changes

serialize our data => formating our data so that it can be tranfered over the internet json => data format that makes it easy to be transered over the internet(make_response)

[<Post 1>] => we can not transfer this over the internet, what will is to convert it into a dictionary(serialize) then convert it into a json object

flask sqlalchemy relationship => one-to-one, one-to-many, many-to-many

seed our database create our first endpoint(API)

{ "id" : 1, "post_title": "weather", "post_content": "It's rainy today" }

to_dict() => convert into a dictionary => to_dict(rule=()), to_dict(only=()) serialize_rule => which fields to exempt serialize_only => which fields to include

user=> user-posts

user mode id posts = db.relationship('Post', back_populates="user")

post mode id user_id= foreignKey user = db.relationship('User', back_populates="posts")

user1.posts post1.user

GET all POST GET ON -GET by id PATCH DELETE

get all and post => will use one url get /users post /users

get /users/ delete /users/ patch /users/

{ "id": "post_title": "post_content": user_id :3

}

blueprints

classes

