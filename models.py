"""Models for Blogly."""

# from enum import unique
# from http import server
# from turtle import title
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

db = SQLAlchemy()

default_image_url = 'https://merriam-webster.com/assets/mw/images/article/art-wap-article-main/egg-3442-e1f6463624338504cd021bf23aef8441@1x.jpg'


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column (
        db.Integer,
        primary_key = True,
        autoincrement = True
    )

    first_name = db.Column (
        db.Text,
        nullable = False
    )

    last_name = db.Column (
        db.Text,
        nullable = False
    )

    image_url = db.Column (
        db.Text,
        nullable = True,
        default = default_image_url
    )

    posts = db.relationship("Post", backref="user", cascade="all, delete-orphan")

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def __repr__(self):
        return f"<User {self.first_name} {self.last_name} {self.image_url}>"

class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(
        db.Integer,
        primary_key = True
    )

    title = db.Column(
        db.Text,
        nullable = False
    )

    content = db.Column(
        db.Text,
        nullable = False
    )

    created_at = db.Column(
        db.DateTime,
        nullable = False,
        server_default = func.now()
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey('user.id'),
        nullable = False
    )

    @property
    def friendly_date(self):
        return self.created_at.strftime("%a %b %-d  %Y, %-I:%M %p")

    def __repr__(self):
        return f"<Post {self.title} {self.content} {self.created_at} {self.user_id}>"


class PostTag(db.Model):
    __tablename__ = 'posts_tags'

    post_id = db.Column(
        db.Integer, 
        db.ForeignKey('posts.id'), 
        primary_key = True
    )

    tag_id = db.Column(
        db.Integer, 
        db.ForeignKey('tags.id'), 
        primary_key = True
    )


class Tag(db.Model):
    __tablename__ = 'tags'

    id = db.Column(
        db.Integer,
        primary_key = True
    )

    name = db.Column(
        db.Text,
        nullable = False,
        unique = True
    )

    posts = db.relationship('Post', secondary = 'posts_tags', cascade = 'all, delete', backref = 'tags')



def connect_db(app):
    db.app = app
    db.init_app(app)