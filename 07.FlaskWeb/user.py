from flask import Blueprint , request, session, render_template
from flask import redirect, flash
import json, hashlib, base64
user_bp = Blueprint('user_bp',__name__)

@user_bp.route('/login', methods=['GET','POST'])
def login():
    menu = {'ho':0,'us':0,'cr':0,'sc':0}
    if request.method == 'GET':
        return render_template('/prototype/user/login.html',menu=menu)
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
                session['uid'] = uid        # 세션값을 설정함으로써 사용자가 로그인하였음을 알게 해줌
                return redirect('/')
            else:
                flash('잘못된 pwd')
                return redirect('/user/login')
        except:
            flash('잘못된 id')
            return redirect('/user/register')

@user_bp.route('/logout')
def logout():
    session.pop('uid',None)                 # 설정한 세션값을 삭제
    return redirect('/')

@user_bp.route('/register')
def register():
    menu = {'ho':0,'us':0,'cr':0,'sc':0}
    return render_template('/prototype/user/register.html',menu=menu)