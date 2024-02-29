# Задание №3
# Доработаем задача про студентов
# Создать базу данных для хранения информации о студентах и их оценках в учебном заведении.
# База данных должна содержать две таблицы: "Студенты" и "Оценки".
# В таблице "Студенты" должны быть следующие поля: id, имя, фамилия, группа и email.
# В таблице "Оценки" должны быть следующие поля: id, id студента, название предмета и оценка.
# Необходимо создать связь между таблицами "Студенты" и "Оценки".
# Написать функцию-обработчик, которая будет выводить список всех студентов с указанием их оценок.

from flask import Flask, render_template
from models import db, Student, Evaluation
from config import Config
import random

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)


@app.cli.command('init-db')
def init_db():
    db.create_all()
    print('<< Done >>')


@app.cli.command('fill_student_tables')
def fill_student_tables():
    print('<< Add Student Data >>')
    for i in range(1, 21):
        add_student = Student(
            first_name=f'First_name_{i}',
            last_name=f'Last_name_{i}',
            group=random.randint(1, 20),
            email=f'Email_{i}'
        )
        db.session.add(add_student)
    db.session.commit()
    print('<< Done >>')


@app.cli.command('fill_evaluation_tables')
def fill_evaluation_tables():
    print('<< Add Evaluation Data >>')
    for i in range(1, 11):
        add_evaluation = Evaluation(
            eval=random.randint(1, 5),
            subject=f'Subject_{random.randint(1, 10)}',
            student_id=random.randint(1, 21)
        )
        db.session.add(add_evaluation)
    db.session.commit()
    print('<< Done >>')


@app.route('/')
@app.route('/index')
def index():
    return render_template('base.html')


@app.route('/result/')
def result():
    context = Evaluation.query.all()
    return render_template('result.html', students=context)


if __name__ == '__main__':
    app.run(debug=True)
