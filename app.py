from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '4/15`/2024'


if __name__ == '__main__':
    app.run()
