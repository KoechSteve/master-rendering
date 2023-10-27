# app.py
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///master_rendering.db'
db = SQLAlchemy(app)

# Define User Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)

# Define File Model
class File(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    filename = db.Column(db.String(120), nullable=False)

# Routes
@app.route('/')
def home():
    return "Welcome to Master Rendering"

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Implement user login logic here

    if username in users and users[username]['password'] == password:
            user = User()
            user.id = username
            login_user(user)
            flash('Login successful!', 'success')
            return redirect(url_for('profile'))
        else:
            flash('Login failed. Please check your credentials.', 'error')


    return "Login page"

@app.route('/register', methods=['GET', 'POST'])
def register():
    # Implement user registration logic here

    from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators
from wtforms.validators import DataRequired, Email, EqualTo
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, UserMixin, login_user

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a secure secret key

# Configure SQLAlchemy for the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user_registration.db'
db = SQLAlchemy(app)

# Configure Flask-Bcrypt for password hashing
bcrypt = Bcrypt(app)

# Configure Flask-Login
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

# Define the User model for SQLAlchemy
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

# Create a registration form using Flask-WTF
class RegistrationForm(FlaskForm):
    username = StringField('Username', [validators.Length(min=4, max=25), DataRequired()])
    email = StringField('Email Address', [Email(), DataRequired()])
    password = PasswordField('Password', [validators.Length(min=6), DataRequired()])
    confirm_password = PasswordField('Confirm Password', [EqualTo('password', message='Passwords must match')])
    submit = SubmitField('Register')

# Routes

@app.route('/index.html')
def home():
    return 'Welcome to the Home Page'

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Implement your login logic here

    from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators
from wtforms.validators import DataRequired
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a secure secret key

# Configure SQLAlchemy for the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user_login.db'
db = SQLAlchemy(app)

# Configure Flask-Bcrypt for password hashing
bcrypt = Bcrypt(app)

# Configure Flask-Login
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

# Define the User model for SQLAlchemy
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

# Create a login form using Flask-WTF
class LoginForm(FlaskForm):
    username = StringField('Username', [DataRequired()])
    password = PasswordField('Password', [DataRequired()])
    submit = SubmitField('Login')

# Routes

@app.route('/')
def home():
    return 'Welcome to the Home Page'

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = User.query.filter_by(username=username).first()
        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user)
            flash('Login successful!', 'success')
            return redirect(url_for('profile'))
        else:
            flash('Login failed. Please check your credentials.', 'error')

    return render_template('login.html', form=form)

@app.route('/profile')
@login_required
def profile():
    return f'Hello, {current_user.username}! This is your profile.'

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)





    return 'Login page'

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        
        user = User(username=username, email=email, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You can now log in.', 'success')
        return redirect(url_for('login'))

    return render_template('register.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)



    return "Registration page"

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    # Implement file upload logic here
    return "Upload page"

@app.route('/queue')
def queue():
    # Display the rendering queue
    return "Rendering Queue"

@app.route('/preview/<file_id>')
def preview(file_id):
    # Display a preview of the rendered image
    return f"Preview for File ID {file_id}"

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
