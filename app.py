"""Blogly application."""

from crypt import methods
from email.policy import default
from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User, Post, Tag, PostTag

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'helloworld123'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

default_image_url = 'https://merriam-webster.com/assets/mw/images/article/art-wap-article-main/egg-3442-e1f6463624338504cd021bf23aef8441@1x.jpg'

connect_db(app)
# db.create_all()

@app.route('/')
def home():
    """This route displays the home page"""
    users = User.query.all()
    return render_template('user_list.html', users = users)


@app.route('/', methods=["POST"])
def add_user():
    """This route allows us to add a user to the database using the form"""
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    image_url = request.form['image_url'] or default_image_url

    new_user = User(first_name=first_name, last_name=last_name, image_url=image_url)

    db.session.add(new_user)
    db.session.commit()

    return redirect(f"/users/{new_user.id}")


@app.route('/users/<int:user_id>')
def user_details(user_id):
    """This route displays the user's details if clicked on the user home page"""
    user = User.query.get(user_id)
    return render_template('details.html', user = user)


@app.route('/users/<int:user_id>/edit')
def edit_user(user_id):
    """This route takes us to the edit page where we can edit the name and image of the selected user."""
    user = User.query.get_or_404(user_id)
    return render_template('edit.html', user= user)


@app.route('/users/<int:user_id>/edit', methods = ['POST'])
def save_edit_user(user_id):
    """This route allows us to save whatever changes were made in the edit page to our database, and returns us to the homepage"""
    user = User.query.get_or_404(user_id)
    
    user.first_name = request.form['first_name']
    user.last_name = request.form['last_name']
    user.image_url = request.form['image_url'] or default_image_url

    db.session.add(user)
    db.session.commit()

    return redirect('/')


@app.route('/users/<int:user_id>/delete', methods = ['POST'])
def delete_user(user_id):
    """This route allows us to delete a user completely from our database."""
    user = User.query.get_or_404(user_id)

    db.session.delete(user)
    db.session.commit()

    return redirect('/')


@app.route('/users/<int:user_id>/posts/new_post')
def add_post_page(user_id):
    user = User.query.get_or_404(user_id)
    return render_template('new_post.html', user = user)

@app.route('/users/<int:user_id>/posts/new_post', methods = ['POST'])
def add_post(user_id):
    # user = User.query.get_or_404(user_id)
    title = request.form['title']
    content = request.form['content']
    user_id = user_id

    new_post = Post(title = title, content = content, user_id = user_id)
    db.session.add(new_post)
    db.session.commit()
    
    return redirect(f"/users/{user_id}")


@app.route('/posts/<int:post_id>')
def show_post(post_id):
    post = Post.query.get_or_404(post_id)
    user = User.query.get_or_404(post.user_id)

    return render_template('show_post.html', post = post, user = user)


@app.route('/posts/<int:post_id>/edit')
def edit_post(post_id):
    post = Post.query.get_or_404(post_id)
    user = User.query.get_or_404(post.user_id)
    
    return render_template('edit_post.html', post = post, user = user)


@app.route('/posts/<int:post_id>/edit', methods = ['POST'])
def submit_post_edit(post_id):
    post = Post.query.get_or_404(post_id)
    user = User.query.get_or_404(post.user_id)
    
    post.title = request.form['title']
    post.content = request.form['content']
    
    db.session.add(post)
    db.session.commit()

    return redirect(f"/users/{user.id}")


@app.route('/posts/<int:post_id>/delete', methods = ['POST'])
def delete_post(post_id):
    post = Post.query(post_id)
    user = User.query(post.user_id)

    db.session.delete(post)
    db.session.commit()

    return redirect(f"/users/{user.id}")



@app.route('/tags')
def tag_list():
    tags = Tag.query.all()
    return render_template('tag_list.html', tags = tags)
    

@app.route('/tags/<int:tag_id>')
def tag_details(tag_id):
    tag = Tag.query.get(tag_id)
    return render_template('tag_details.html', tag = tag)


@app.route('/tags/new')
def add_tag_page():
    return render_template('add_tag.html')

    
@app.route('/tags/new',methods=["POST"])
def add_tag():
    # name = request.form['name']
    
    new_tag = Tag(name = request.form['name'])

    db.session.add(new_tag)
    db.session.commit()
    return redirect('/tags')


@app.route('/tags/<int:tag_id>/edit')
def edit_tag_page(tag_id):
    tag = Tag.query(tag_id)

    return render_template('edit_tag.html', tag = tag)




