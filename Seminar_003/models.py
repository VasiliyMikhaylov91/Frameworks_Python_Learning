from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(20), nullable=False)
    lastname = db.Column(db.String(20), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(3), nullable=False)
    group = db.Column(db.String(60), nullable=False)
    id_faculty = db.Column(db.Integer, db.ForeignKey('faculty.id'))

    def __repr__(self):
        return f'{self.firstname} {self.lastname}'


class Faculty(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    faculty_name = db.Column(db.String(80), unique=True, nullable=False)
    students = db.relationship('Student', backref='faculty', lazy=True)

    def __repr__(self):
        return f'{self.faculty_name}'
