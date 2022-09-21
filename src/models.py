from flask_sqlalchemy import SQLAlchemy
from eralchemy import render_er

db = SQLAlchemy()


class Follower(db.Model):
   
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    user_to = db.Column(db.Integer)
    user_from = db.Column(db.Integer)


class Likes(db.Model):
    
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    like = db.Column(db.Integer)
       

class Media(db.Model):
    
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(250), nullable=False)
    url = db.Column(db.String(250))
    tag = db.Column(db.String(250))
    likes_id = db.Column(db.Integer, db.ForeignKey('likes.id'))
    likes = db.relationship(Likes)

class Post(db.Model):
    
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(250), nullable=False)
    media_id = db.Column(db.Integer, db.ForeignKey('media.id'))
    media = db.relationship(Media) 
      

class Profile(db.Model):
    
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250), nullable=False)
    username = db.Column(db.String(250), nullable=False)
    bio = db.Column(db.String(250))
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))
    post = db.relationship(Post)
    user_to_id = db.Column(db.Integer, db.ForeignKey('follower.id'))
    follower = db.relationship(Follower)
    user_from_id = db.Column(db.Integer, db.ForeignKey('follower.id'))
    follower= db.relationship(Follower)

 
   



    
    
  
  
            
    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(db.Model, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e