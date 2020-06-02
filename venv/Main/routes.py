from flask import Blueprint,render_template,request
from venv.models import Post
from venv.User.utils import save_theme,save_picture,send_reset_email

main = Blueprint('main',__name__)


@main.route("/")
@main.route("/home",methods= ['GET','POST'])
def home():
    #form = PostForm
    page=request.args.get('page',1,type=int)
    posts= Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=6)
    return render_template('home.html', posts=posts)

@main.route("/about")
def about():
    return render_template('about.html', title='Welcome')
