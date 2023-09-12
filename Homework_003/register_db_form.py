from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from forms import RegistrationForm
from models import db, User
from werkzeug.security import generate_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
app.config['SECRET_KEY'] = '7a7e6b6b3385269194393a19da4a8aa3b5dcb2095a6d8a6838a9909f7cad4fa4'
db.init_app(app)
csrf = CSRFProtect(app)


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('OK')


@app.route('/')
def hi():
    return 'Hi'


@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        hash_passwd = generate_password_hash(request.form.get('password'))
        new_user = User(firstname=request.form.get('firstname'),
                        lastname=request.form.get('lastname'),
                        email=request.form.get('email'),
                        passwd=hash_passwd)
        db.session.add(new_user)
        db.session.commit()
        pass
    return render_template('register.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
