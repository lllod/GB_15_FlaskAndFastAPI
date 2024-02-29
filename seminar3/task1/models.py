from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    group = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    evaluation = db.relationship('Evaluation', backref='student', lazy=True)

    def __repr__(self):
        return f"Student({self.id}, {self.first_name}, {self.last_name}, {self.group}, {self.email})"


class Evaluation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    eval = db.Column(db.Integer, nullable=False)
    subject = db.Column(db.String(30), nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)

    def __repr__(self):
        return f"Evaluation({self.id}, {self.eval}, {self.subject})"

