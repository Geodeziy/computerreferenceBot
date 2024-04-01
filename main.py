from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('/index.html', title='index')


if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0', ssl_context=('C:/crt/cert.pem', 'C:/crt/key.pem'))