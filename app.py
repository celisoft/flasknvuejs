from flask import Flask, render_template


class VueFlask(Flask):
    jinja_options = Flask.jinja_options.copy()
    jinja_options.update(dict(
        block_start_string='(%',
        block_end_string='%)',
        variable_start_string='((',
        variable_end_string='))',
        comment_start_string='(#',
        comment_end_string='#)'
    ))


app = VueFlask(__name__, template_folder='templates', static_folder='static')


@app.route('/')
def test():
    message = "This is a test with Flask, Jinja2 & VueJS !"
    return render_template('index.html', message=message)


if __name__ == '__main__':
    app.run()
