from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello world'


@app.route('/about/')
def about():
    return "It's about"


@app.route('/contact/')
def contact():
    return "It's contact"


@app.route('/<int:num_1>/<int:num_2>/')
def sum_nums(num_1: int, num_2: int) -> str:
    return f'{num_1 + num_2}'


@app.route('/length/<string:inp>/')
def len_str(inp: str) -> str:
    return f'{len(inp)}'


@app.route('/first')
def first():
    return render_template('base.html')


@app.route('/students/')
def students():
    student_list = [
        {
            'firstname': 'Имя',
            'lastname': 'Фамилия',
            'age': 'Возраст',
            'average': 'Средний балл',
        },
        {
            'firstname': 'Иван',
            'lastname': 'Иванов',
            'age': 18,
            'average': 4.8
        },
        {
            'firstname': 'Петр',
            'lastname': 'Петров',
            'age': 19,
            'average': 4.3,
        },
        {
            'firstname': 'Сидр',
            'lastname': 'Сидоров',
            'age': 20,
            'average': 4.5,
        }
    ]
    return render_template('students.html', student_list=student_list)


if __name__ == '__main__':
    app.run()
