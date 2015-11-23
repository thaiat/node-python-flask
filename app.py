import os
import sys
import time
from flask import Flask, request, jsonify
import json
import logging

app = Flask(__name__)
app.logger.setLevel(logging.DEBUG)  # set the desired logging level here


@app.route("/")
def index():
    return "Welcome Heroku Flask!"


@app.route('/api/videos/process', methods=['POST'])
def videos_process():
    t0 = time.clock()
    content = request.get_json(silent=True)
    app.logger.debug('A value for debugging')
    app.logger.warning('A value for warning')
    print(content.get('id').get('b'))
    print(time.clock() - t0)
    list = [
        {'param': 'foo', 'val': 2},
        {'param': 'bar', 'val': 10}
    ]
    # jsonify will do for us all the work, returning the
    # previous data structure in JSON
    # return jsonify(results = list)
    return json.dumps(list)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.debug = True
    app.run(host='0.0.0.0', port=port)
