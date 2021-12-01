from flask import Flask
from requests import get

app = Flask(__name__)
SITE_NAME = 'http://68.225.115.149:8081/'

@app.route('/')
def proxy():
  return get(f'{SITE_NAME}').content

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)