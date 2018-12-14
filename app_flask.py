import config

from flask import Flask, request
from main import service_webhook

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def root():
    request_json = request.get_json()
    request_args = request.args
    print(request_json, request_args)
    return "Root Works!"


@app.route("/service_webhook", methods=['GET', 'POST'])
def get_webhook():
    return service_webhook(request)


# For local run
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
