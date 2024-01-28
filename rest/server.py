from flask import Flask, request

app = Flask(__name__)


@app.route('/add', methods=['GET'])
def add_numbers():
    num1 = int(request.args.get('num1'))
    num2 = int(request.args.get('num2'))
    result = num1 + num2
    return {'result': result}


if __name__ == '__main__':
    app.run()
