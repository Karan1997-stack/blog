from flask import Blueprint,render_template,url_for,flash,redirect,request,abort
from flask_login import current_user, login_required
from venv import db
from venv.models import Post
from venv.Post.forms import PostForm
from venv.User.utils import save_theme,save_picture,send_reset_email,formatter

posts = Blueprint('posts',__name__)





@posts.route("/post/new", methods=['GET','POST'])
@login_required
def new_post():
    pather=""
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, author=current_user)
        post.title = form.title.data
        post.content = form.content.data
        if form.theme.data:
            theme_file = save_theme(form.theme.data)
            post.theme = theme_file
        else:
            theme_file = url_for('static', filename='post_pics/blog_default')
        p1=Post.query.filter_by(title=form.title.data).first()
        if p1:
            Post.theme=theme_file
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!','success')
        return redirect(url_for('main.home'))
    elif request.method == 'GET':
        theme_file = url_for('static', filename='post_pics/blog_default')

    theme_file = url_for('static', filename='post_pics/blog_default')

    return render_template('create_post.html',title='New Post',content=form.content.data,form=form,legend='Create Post')


@posts.route("/post/<int:post_id>")
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title,post=post)



@posts.route("/post/<int:post_id>/update", methods=['GET','POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title=form.title.data
        post.content=form.content.data
        if form.theme.data:
            theme_file = save_theme(form.theme.data)
            post.theme = theme_file
        else:
            theme_file = url_for('static', filename='post_pics/blog_default')

        db.session.commit()
        flash("Your post has been updated!", 'success')
        return redirect(url_for('posts.post',post_id=post.id))
    elif request.method== 'GET':
        form.title.data = post.title
        form.content.data = post.content
        form.theme.data = post.theme

    return render_template('create_post.html',title='Update Post',content=form.content.data,form=form,legend='Update Post')


@posts.route("/post/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted','success')
    return redirect(url_for('main.home'))


