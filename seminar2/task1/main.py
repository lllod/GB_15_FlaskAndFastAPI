# Задание №4
# Создать страницу, на которой будет форма для ввода текста и кнопка "Отправить"
# При нажатии кнопки будет произведен подсчет количества слов в тексте и переход на страницу с результатом.


from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)


@app.get('/')
def index_get():
    return render_template('base.html')


@app.post('/')
def index_post():
    message = request.form.get('text')
    return redirect(url_for('result', message=message))


@app.route('/result/<message>')
def result(message):
    message_len = len(message)
    return render_template('result.html', result=message_len)


if __name__ == '__main__':
    app.run(debug=True)
