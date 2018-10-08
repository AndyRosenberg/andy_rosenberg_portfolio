from flask import Blueprint, request
from app import *

bp = Blueprint('blog', __name__)

@bp.route('/index', methods=['GET'])
def index():
    cursor = Blog.select().order_by(Blog.created_date.desc())
    return render_template('index.html', cursor=cursor)

bp.add_url_rule('/', 'index', index)

@bp.route('/auth', methods=['GET', 'POST'])
def authenticate():
    if request.method == 'POST':
        if request.form['password'].strip() == os.environ['PORTFOLIO_AUTH']:
            session['admin'] = True
            return redirect('/blog/create')
        else:
            return redirect('/blog/auth')
    else:
        return render_template('auth.html')

@bp.route('/create', methods=['GET', 'POST'])
def create():
    if 'admin' in session:
        if request.method == 'GET':
            return render_template('create.html')
        else:
            ttl = request.form['title']
            bdy = "\n\n".join(request.form['body'].splitlines())
            img = request.form['image'].strip()
            if ttl and bdy:
                im_blog = Blog(title=ttl, body=bdy, image=img) if img else Blog(title=ttl, body=bdy) 
                im_blog.save()
                return redirect('/blog')
            else:
                return redirect('/blog/create')
    else:
        return redirect('/blog/auth')
