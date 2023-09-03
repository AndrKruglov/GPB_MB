from Package import db


class User(db.Model):
    clients_ID = db.Column(db.Integer, primary_key=True)
    e_mail = db.Column(db.String(30), unique=True, nullable=False)
    client_password_hash = db.Column(db.String(250), unique=True, nullable=False)


class Clients(db.Model):
    clients_ID = db.Column(db.Integer, primary_key=True)
    fio = db.Column(db.String(90), unique=True, nullable=False)
    e_mail = db.Column(db.String(30), unique=True, nullable=False)
    client_password_hash = db.Column(db.String(250), unique=True, nullable=False)


class Accounts(db.Model):
    accounts_id = db.Column(db.Integer, nullable=False, primary_key=True)
    clients_id = db.Column(db.Integer, nullable=False)
    account_no = db.Column(db.String(20), nullable=False)
    account_summa = db.Column(db.Numeric(20), nullable=False)
    percent = db.Column(db.String(20), nullable=False)
