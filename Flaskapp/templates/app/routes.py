from flask import Blueprint, render_template, url_for, flash, redirect, request
from app import db
from app.forms import PostForm
from app.models import Post
from flask_login import current_user, login_required

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    posts = Post.query.all()
    return render_template('index.html', posts=posts)

@bp.route('/post/new', methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('main.index'))
    return render_template('create_post.html', title='New Post', form=form)

@bp.route('/post/<int:post_id>')
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)
