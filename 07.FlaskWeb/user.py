from flask import Blueprint , request, session, render_template
from flask import redirect, flash
import json, hashlib, base64
user_bp = Blueprint('user_bp',__name__)

@user_bp.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('/prototype/login.html')
    else:
        uid = request.form['uid']
        pwd = request.form['pwd']
        with open('static/data/password.txt') as f:
            s = f.read()
        passwords = json.loads(s)
        try:
            db_pwd = passwords[uid]
            pwd_sha256 = hashlib.sha256(pwd.encode())
            hashed_pwd = base64.b64encode(pwd_sha256.digest()).decode('utf-8')
            if hashed_pwd == db_pwd:
                flash('good')
                return redirect('/')
            else:
                flash('잘못된 pwd')
                return redirect('/user/login')
        except:
            flash('잘못된 id')
            return redirect('/user/register')
        
@user_bp.route('/register')
def register():
    return '<h1>회원 가입 페이지 입니다.</h1>'