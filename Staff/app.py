from flask import Flask,request,jsonify,session
from models import User,Token,db
from flask_bcrypt import Bcrypt
from flask_login import LoginManager,logout_user,login_user,login_required,current_user
from datetime import datetime,timedelta
import secrets

app  = Flask('__name__')
app.config['SECRET_KEY'] = 'chuks'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///staff.db'
db.init_app(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

def generate_token(user_id):
    token = secrets.token_urlsafe(10)
    now =datetime.utcnow()
    ended_at = now + timedelta(days=1)
    new_token=Token(user_id = user_id,token=token,created_at=now,ended_at=ended_at)
    db.session.add(new_token)
    db.session.commit()
    return token

@app.route('/api/register',methods=['POST'])
def register():
    try:
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        if not username or not password:
            return jsonify({'message':'username and password are required'})

        hashed_pw= bcrypt.generate_password_hash(password)
        new_user =User(username=username,password=hashed_pw)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message':'you have successfully registered'}),200
    except Exception as e:
        return jsonify({'message':'internal server error','error':str(e)}),500


@app.route('/api/login',methods=['POST'])
def login():
    try:
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        if not username or not password:
            return jsonify({'message':'username and password invalid try again'}),400

        user = User.query.filter_by(username=username).first()
        if user and bcrypt.check_password_hash(user.password,password):
            login_user(user)
            token = generate_token(user.id)
            db.session.commit()
            return jsonify({'message':'You have successfully login in','token': token}),200
        return jsonify({'message':'invalid credentials'}),401
    except Exception as e:
        return jsonify({'message':'internal server error','error':str(e)}),500

@app.route('/api/logout',methods=['GET'])
def logout():
    try:
        Token.query.filter_by(user_id=current_user.id, is_active=True).update({"is_active": False})
        db.session.commit()
        load_user()
        return jsonify({'message':'You have been logout'}),200
    except Exception as e:
        return jsonify({'message':'internal server error','error':str(e)}),500

@app.route('/api/protected',methods=['GET'])
@login_required
def protected():
    try:
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return jsonify({'message':'Token is missing'}),401


        parts = auth_header.split(" ")

        if len(parts) != 2:
            return jsonify({'message': 'Invalid token format'}), 401

        token = parts[1]
        token_obj = Token.query.filter_by(user_id=current_user.id, token=token, is_active=True).first()

        if token_obj and datetime.utcnow() < token_obj.ended_at:
            return jsonify({'message':'Access granted'}),200
        return jsonify({'message':'invalid or expired token'}),400
    except Exception as e:
        return jsonify({'message':'internal server error','error':str(e)}),500


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.run(debug=True)
