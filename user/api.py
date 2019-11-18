from flask import request, jsonify, url_for
from flask_mail import Mail, Message
from itsdangerous import URLSafeTimedSerializer, SignatureExpired

from run import app, db
from user.models import User

mail = Mail(app)
serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])


@app.route("/user")
def user_index():
    return "Hello World"


@app.route('/user/register', methods=['POST'])
def register_user():
    try:
        username = request.json['username']
        email = request.json['email']
        passw = request.json['password']

        new_user = User(username, email, passw)

        db.session.add(new_user)
        db.session.commit()
        db.session.close()

        send_email(email)

        resp = jsonify({"Action": 'User Registered Successfully'})
        resp.status_code = 200
        return resp

    except Exception as e:
        resp = jsonify({"error": e.__str__()})
        resp.status_code = 200
        return resp


@app.route('/user/login', methods=['POST'])
def login_user():
    try:
        email = request.json['email']
        passw = request.json['password']
        check = db.session.query(User).filter(User.email == email).filter(User.password == passw).all()
        if check.__len__() == 1:
            if check[0].verified:
                resp = jsonify({"Action": 'User Logged In Successfully'})
                resp.status_code = 200
                return resp
            else:
                resp = jsonify({"error": 'User email is not verified'})
                resp.status_code = 200
                return resp

        else:
            resp = jsonify({"Action": 'User Login Failure', "reason": "Email or Password Incorrect"})
            resp.status_code = 200
            return resp

    except Exception as e:
        resp = jsonify({"error": e.__str__()})
        resp.status_code = 200
        return resp


@app.route('/confirm_email/<token>')
def confirm_email(token):
    try:
        email = serializer.loads(token, salt='confirm_email', max_age=86400)
        User.confirm_email(db, email)
        db.session.commit()
        db.session.close()

    except SignatureExpired:
        return jsonify({"error": "The email link Expired"})

    return jsonify({"action": "The Email is confirmed"})


def send_email(email):
    token = serializer.dumps(email, salt='confirm_email')

    msg = Message('Confirm Email', recipients=[email])
    link = url_for('confirm_email', token=token, _external=True)
    msg.body = "press the link to confirm your email {}".format(link)
    mail.send(msg)
