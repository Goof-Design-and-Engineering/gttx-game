from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/', methods=['POST'])
def make_post_request():
    url = '<CHANGEME>'
    data = {'key': 'value'}
    response = requests.post(url, data=data)
    return response.text

if __name__ == '__main__':
    app.run()
