from flask import Flask, render_template, url_for, request, make_response

app = Flask(__name__)


@app.get('/')
def form():
    if name := request.cookies.get('username'):
        return render_template('greetings.html', title='greetings', name=name)
    return render_template('/index.html/')


@app.post('/')
def greetings():
    if name := request.form.get('name'):
        context = {
            'title': 'greetings',
            'name': name
        }
        response = make_response(render_template('greetings.html', **context))
        response.headers['new_head'] = 'New_value'
        response.set_cookie('username', context['name'])
        return response
    return render_template('/index.html/')


@app.route('/greetings_exit.html/')
def logout():
    response = make_response(render_template('/index.html/'))
    response.delete_cookie('username')
    return response


if __name__ == '__main__':
    app.run(debug=True)
