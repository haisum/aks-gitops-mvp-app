from flask import Flask
from flask import abort
from prometheus_flask_exporter import PrometheusMetrics

import lorem
import logging


app = Flask(__name__)

# Disable accessive logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

@app.route('/error/500')
def error500():
    abort(500, description="internal server error")

@app.route('/')
def hello_world():
    return 'Flask: Hello World from feature test Canary Deployment v25'


def version():
    return 'V25'


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
    metrics = PrometheusMetrics(app)

    # static information as metric
    metrics.info('helloworld_info', 'Hello world info', version='25')
