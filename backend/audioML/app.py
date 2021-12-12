from flask import Flask
from flask import render_template
from flask import request, jsonify
import audio_processor as ap
import time
'''Implementation of audio API using url params'''

app = Flask(__name__)


@app.route('/test')
def get_current_time():
    return {'time': time.time()}

def main():
    count = 0 
    if count < 1:
        #host = input("Enter the IP address of your PI or `localhost` for local development: ")
        count += 1
        app.run(host='localhost', port = 5000, debug=True)

if __name__ == '__main__':
    main()