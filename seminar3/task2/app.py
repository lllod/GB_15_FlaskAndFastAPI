# Задание №4
# Создайте форму регистрации пользователя с использованием Flask-WTF. Форма должна содержать следующие поля:
# ○ Имя пользователя (обязательное поле)
# ○ Электронная почта (обязательное поле, с валидацией на корректность ввода email)
# ○ Пароль (обязательное поле, с валидацией на минимальную длину пароля)
# ○ Подтверждение пароля (обязательное поле, с валидацией на совпадение с паролем)
# После отправки формы данные должны сохраняться в базе данных (можно использовать SQLite) и выводиться сообщение об
# успешной регистрации. Если какое-то из обязательных полей не заполнено или данные не прошли валидацию, то должно
# выводиться соответствующее сообщение об ошибке.
# Дополнительно: добавьте проверку на уникальность имени пользователя и электронной почты в базе данных.
# Если такой пользователь уже зарегистрирован, то должно выводиться сообщение об ошибке.


from flask import Flask, render_template, request, redirect, url_for
from models import db, Users
from config import Config
from models_form import RegistrationForm
from flask_wtf.csrf import CSRFProtect


app = Flask(__name__)
app.config.from_object(Config)
csrf = CSRFProtect(app)
db.init_app(app)


@app.cli.command('init-db')
def init_db():
    print('<< DataBase Created >>')
    db.create_all()
    print('<< Done >>')


@app.route('/registration/', methods=['GET', 'POST'])
def registration():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        username = form.username.data
        email = form.email.data
        if Users.query.filter_by(username=username).first():
            return redirect(url_for('error_form', error='Dublicate username!'))
        elif Users.query.filter_by(email=email).first():
            return redirect(url_for('error_form', error='Dublicate email!'))
        print('<< ADD User >>')
        add_user = Users(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data
        )
        db.session.add(add_user)
        db.session.commit()
        print('<< ADD User DONE >>')
        return redirect(url_for('result'))
    return render_template('registration.html', form=form)


@app.route('/')
def index():
    return render_template('base.html')


@app.route('/result')
def result():
    return render_template('result.html')


@app.route('/error-form/<error>')
def error_form(error):
    return render_template('error-form.html', error=error)


if __name__ == '__main__':
    app.run(debug=True)
