from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html', title='Домашняя')


@app.route('/clothes/')
def clothes():
    cloth_list = [
        {'picture': '/static/images/gray-blazer.jpg',
         'title': 'Серый блейзер',
         'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. '
                        'Consequuntur cumque eum facilis iste omnis sint tempore ullam velit? '
                        'Aperiam autem consectetur maxime nihil qui. Molestiae.'
         },
        {
            'picture': '/static/images/Camperas_sofi.jpg',
            'title': 'Кемпер',
            'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. '
                           'Consequuntur cumque eum facilis iste omnis sint tempore ullam velit? '
                           'Aperiam autem consectetur maxime nihil qui. Molestiae.'
        },
        {
            'picture': '/static/images/jeans-shirt.jpg',
            'title': 'Джинсовая рубашка',
            'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. '
                           'Consequuntur cumque eum facilis iste omnis sint tempore ullam velit? '
                           'Aperiam autem consectetur maxime nihil qui. Molestiae.'
        }
    ]
    return render_template('clothes.html', title='Одежда', cloth_list=cloth_list)


@app.route('/jackets/')
def jackets():
    jackets_list = [
        {'picture': '/static/images/American_Bombshell.jpg',
         'title': 'Американская сенсация',
         'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. '
                        'Consequuntur cumque eum facilis iste omnis sint tempore ullam velit? '
                        'Aperiam autem consectetur maxime nihil qui. Molestiae.'
         },
        {
            'picture': '/static/images/Bomber_Jacket.jpg',
            'title': 'Бомбер',
            'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. '
                           'Consequuntur cumque eum facilis iste omnis sint tempore ullam velit? '
                           'Aperiam autem consectetur maxime nihil qui. Molestiae.'
        },
        {
            'picture': '/static/images/Windjack.jpg',
            'title': 'Ветровка',
            'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. '
                           'Consequuntur cumque eum facilis iste omnis sint tempore ullam velit? '
                           'Aperiam autem consectetur maxime nihil qui. Molestiae.'
        }
    ]
    return render_template('jackets.html', title='Куртки', jackets_list=jackets_list)


@app.route('/shoes/')
def shoes():
    shoes_list = [
        {'picture': '/static/images/Footwear_Shoes.jpg',
         'title': 'Кеды',
         'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. '
                        'Consequuntur cumque eum facilis iste omnis sint tempore ullam velit? '
                        'Aperiam autem consectetur maxime nihil qui. Molestiae.'
         },
        {
            'picture': '/static/images/King_Street_Sneak.JPG',
            'title': 'Королевские туфли',
            'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. '
                           'Consequuntur cumque eum facilis iste omnis sint tempore ullam velit? '
                           'Aperiam autem consectetur maxime nihil qui. Molestiae.'
        },
        {
            'picture': "/static/images/Shoes,_pair_woman's.jpg",
            'title': 'Женские броги',
            'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. '
                           'Consequuntur cumque eum facilis iste omnis sint tempore ullam velit? '
                           'Aperiam autem consectetur maxime nihil qui. Molestiae.'
        }
    ]
    return render_template('shoes.html', title='Обувь', shoes_list=shoes_list)


if __name__ == '__main__':
    app.run(debug=True)
