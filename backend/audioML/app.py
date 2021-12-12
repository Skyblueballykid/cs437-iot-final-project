from flask import Flask
from flask import render_template
from flask import request, jsonify
import audio_processor as ap

'''Implementation of audio API using url params'''

app = Flask(__name__)





@app.route('/', methods=["POST"])
def post():
    label = ap.process_wav()
    data = request.get_json()
    print(data['msg'])
    res = {'status': 'ok'}
    return jsonify(res)


def main():
    count = 0 
    if count < 1:
        host = input('localhost')
        count += 1
        app.run(host=host, port = 8080, debug=True)

    

if __name__ == '__main__':
    main()