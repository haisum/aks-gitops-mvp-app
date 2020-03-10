from flask import Flask
import lorem
import logging


app = Flask(__name__)

# Disable accessive logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

@app.route('/')
def hello_world():
    return 'Flask: Hello World from Canary Deployment v7'


@app.route('/version')
def version():
    return 'V7'


@app.route('/log')
def log():
    paragraph = lorem.paragraph()
    print(paragraph, flush = True)
    return paragraph

@app.route('/api')
def rest_hello_world():
    return '{"id":1,"message":"Flask: Hello World from Canary Deployment"}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9898)