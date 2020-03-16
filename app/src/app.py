from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Flask: Hello World from Docker'


@app.route('/version')
def hello_world():
    return '9.0'

@app.route('/api')
def rest_hello_world():
    return '{"id":1,"message":"Flask: Hello World from Docker"}'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9898)