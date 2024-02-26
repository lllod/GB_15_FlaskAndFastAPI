# Задание №5
# Создать страницу, на которой будет форма для ввода двух чисел и выбор операции (сложение, вычитание, умножение
# или деление) и кнопка "Вычислить"
# При нажатии на кнопку будет произведено вычисление результата выбранной операции и переход на страницу с результатом.

from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)


@app.get('/')
def index_get():
    return render_template('base.html')


@app.post('/')
def index_post():
    first_num = int(request.form.get('num1'))
    second_num = int(request.form.get('num2'))
    operation = request.form.get('operation')
    match operation:
        case '+':
            result_num = first_num + second_num
        case '-':
            result_num = first_num - second_num
        case '*':
            result_num = first_num * second_num
        case '/':
            result_num = first_num / second_num
    return redirect(url_for('result', num_res=result_num))


@app.route('/result/<num_res>')
def result(num_res):
    return render_template('result.html', result=num_res)


if __name__ == '__main__':
    app.run(debug=True)
