import os
from flask import Flask, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'mysecret'

# ✅ DATABASE CONFIG (POSTGRES FIX)
db_url = os.environ.get('DATABASE_URL')

if db_url:
    if db_url.startswith("postgres://"):
        db_url = db_url.replace("postgres://", "postgresql://", 1)
else:
    # fallback for local
    db_url = "sqlite:///finance.db"

app.config['SQLALCHEMY_DATABASE_URI'] = db_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# ---------------- MODELS ----------------

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(100))
    amount = db.Column(db.Float)
    type = db.Column(db.String(10))
    date = db.Column(db.String(20))
    user = db.Column(db.String(50))


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(200))


# ---------------- ROUTES ----------------

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = generate_password_hash(request.form['password'])

        # ✅ duplicate user check
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            return "User already exists"

        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()

        return redirect('/login')

    return render_template('signup.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            session['user'] = username
            return redirect('/')
        else:
            return "Invalid credentials"

    return render_template('login.html')


@app.route('/')
def index():
    if 'user' not in session:
        return redirect('/login')

    data = Transaction.query.filter_by(user=session['user']).all()

    income = sum(t.amount for t in data if t.type == "Income")
    expense = sum(t.amount for t in data if t.type == "Expense")
    balance = income - expense

    return render_template(
        'index.html',
        data=data,
        income=income,
        expense=expense,
        balance=balance
    )


@app.route('/add', methods=['GET', 'POST'])
def add():
    if 'user' not in session:
        return redirect('/login')

    if request.method == 'POST':
        desc = request.form['description']
        amount = float(request.form['amount'])
        t_type = request.form['type']
        date = request.form['date']

        new_data = Transaction(
            description=desc,
            amount=amount,
            type=t_type,
            date=date,
            user=session['user']  # ✅ user mapping
        )

        db.session.add(new_data)
        db.session.commit()

        return redirect('/')

    return render_template('add.html')


@app.route('/delete/<int:id>')
def delete(id):
    if 'user' not in session:
        return redirect('/login')

    data = Transaction.query.get(id)

    # ✅ SECURITY: only delete own data
    if data and data.user == session['user']:
        db.session.delete(data)
        db.session.commit()

    return redirect('/')


@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/login')


# ---------------- DB INIT ----------------

with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True)