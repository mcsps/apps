from flask import Flask, request
from prometheus_flask_exporter import PrometheusMetrics
from os import environ

app = Flask(__name__)

app.secret_key = 'your-secret-key'

metrics = PrometheusMetrics(app)
metrics.info('app_info', 'Application info', version='1.0.3')

@app.route('/a', methods=['GET', 'POST'])
def a():
    message = "You requested: a"
    return message, 200, {'Content-Type': 'text/plain'}

@app.route('/b', methods=['GET', 'POST'])
def a():
    message = "You requested: b"
    return message, 200, {'Content-Type': 'text/plain'}

@app.route('/c', methods=['GET', 'POST'])
def a():
    message = "You requested: c"
    return message, 200, {'Content-Type': 'text/plain'}

@app.errorhandler(404)
def not_found_error(error):
    message = "Couldn't found your requested page"
    return message, 404, {'Content-Type': 'text/plain'}

@app.errorhandler(500)
def internal_error(error):
    message = "Something went wrong"
    return message, 404, {'Content-Type': 'text/plain'}

if __name__ == '__main__':

  app.run(
    host = "0.0.0.0",
    port = 9091,
    debug = 0
  )
