from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy import ForeignKey, MetaData
from datetime import datetime


metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy()

class Profile(db.Model, SerializerMixin):
    __tablename__ = 'profile_table'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    birthday = db.Column(db.Date, nullable=True)
    profile_picture = db.Column(db.String(500), nullable=True)
    description = db.Column(db.String(400))

    posts = db.relationship('Post', backref='profile')
    comments = db.relationship('Comment', backref='profile')
    messages = db.relationship('Message', backref='profile')


    def __repr__(self):
        return f'<Profile {self.id}>'
    

class Post(db.Model, SerializerMixin):
    __tablename__ = 'post_table'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    profile_id = db.Column(db.Integer, ForeignKey('profile_table.id'), nullable=False)

    comments = db.relationship('Comment', backref='post')
    profile = db.relationship('Profile', backref='post')

    def __repr__(self):
        return f'<Post {self.id}>'
    
class Comment(db.Model, SerializerMixin):
    __tablename__ = 'comment_table'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    post_id = db.Column(db.Integer, ForeignKey('post_table.id'), nullable=False)
    profile_id = db.Column(db.Integer, ForeignKey('profile_table.id'), nullable=False)

    post = db.relationship('Post', backref='comment')
    profile = db.relationship('Profile', backref='comment')

    def __repr__(self):
        return f'<Comment {self.id}>'
    
class Message(db.Model, SerializerMixin):
    __tablename__ = 'message_table'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    sender_profile_id = db.Column(db.Integer, ForeignKey('profile_table.id'), nullable=False)
    receiver_profile_id = db.Column(db.Integer, ForeignKey('profile_table.id'), nullable=False)

    sender_profile = db.relationship('Profile', foreign_keys=[sender_profile_id], backref='message')
    receiver_profile = db.relationship('Profile', foreign_keys=[receiver_profile_id], backref='message')

    def __repr__(self):
        return f'<Message {self.id}>'