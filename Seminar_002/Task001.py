from flask import Flask, render_template, url_for, request

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('/index.html/')


@app.get('/task1/')
def task1_get():
    return render_template('/greetings_form.html/')


@app.post('/task1/')
def task1_post():
    if name := request.form.get('name'):
        return render_template('/greetings.html/', name=name)
    return render_template('/greetings.html/', name='Незнакомец')


if __name__ == '__main__':
    app.run(debug=True)
