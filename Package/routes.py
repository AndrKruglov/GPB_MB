from flask import render_template, request, redirect, flash, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user

from Package import app, db
from Package.models import Clients


@app.route('/', methods=['GET'])
def hello_world():
    return render_template('hello.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    if email and password:
        user = Clients.query.filter_by(e_mail=email).first()

        if user and check_password_hash(user.client_password_hash, password):
            login_user(user)

            return redirect(url_for('registration'))

        else:
            flash('e_mail or password is not correct')

    else:
        flash('please fill e_mail and password')
    return render_template("index.html")


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    if request.method == 'POST':
        fio = request.form['fio']
        email = request.form['email']
        user = Clients.query.filter_by(e_mail=email).first()
        if user:
            return 'User with this email already exists'
        else:
            # password = request.form['password']
            password = generate_password_hash('password')
            user = Clients(fio=fio, e_mail=email, client_password_hash=password)
            db.session.add(user)
            db.session.commit()
            return 'User registered successfully'
    else:
        return render_template("registration.html")


@app.route('/clients', methods=['GET'])
def get_clients():
    clients = Clients.query.all()
    return render_template('clients.html', clients=clients)
