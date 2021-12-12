from flask import Flask
from flask import render_template
from flask import request, jsonify
from flask_cors import CORS, cross_origin
#import audio_processor as ap
import time
'''Implementation of audio API using url params'''

app = Flask(__name__)
CORS(app, support_credentials=True)

@app.route('/test')
@cross_origin(supports_credentials=True)
def get_current_time():    
    response = jsonify({'time': time.time()})
    return response

def main():
    count = 0 
    if count < 1:
        #host = input("Enter the IP address of your PI or `localhost` for local development: ")
        count += 1
        app.run(host='localhost', port = 5000, debug=True)

if __name__ == '__main__':
    main()