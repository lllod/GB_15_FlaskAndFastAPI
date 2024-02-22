# Задание №7
# Написать функцию, которая будет выводить на экран HTML страницу с блоками новостей.
# Каждый блок должен содержать заголовок новости, краткое описание и дату публикации.
# Данные о новостях должны быть переданы в шаблон через контекст.


from flask import Flask, render_template
from datetime import date

app = Flask(__name__)

news_list = [{'title': 'News 1',
              'date': str(date.today()),
              'text': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aliquam ea et ex fugit illo molestias \
                      temporibus! Animi consequatur minus reprehenderit!'},
             {'title': 'News 2',
              'date': str(date.today()),
              'text': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aliquam ea et ex fugit illo molestias \
                      temporibus! Animi consequatur minus reprehenderit!'},
             {'title': 'News 3',
              'date': str(date.today()),
              'text': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aliquam ea et ex fugit illo molestias \
                      temporibus! Animi consequatur minus reprehenderit!'},
             {'title': 'News 4',
              'date': str(date.today()),
              'text': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aliquam ea et ex fugit illo molestias \
                      temporibus! Animi consequatur minus reprehenderit!'},
             {'title': 'News 5',
              'date': str(date.today()),
              'text': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aliquam ea et ex fugit illo molestias \
                      temporibus! Animi consequatur minus reprehenderit!'},
             {'title': 'News 6',
              'date': str(date.today()),
              'text': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aliquam ea et ex fugit illo molestias \
                      temporibus! Animi consequatur minus reprehenderit!'},
             ]
context = {'news': news_list}


@app.route('/')
def hello_world():
    return render_template('base.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
