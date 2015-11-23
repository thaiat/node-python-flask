import os
import sys
import time
from flask import Flask, request, jsonify
import json
import logging
import video
app = Flask(__name__)
app.logger.setLevel(logging.DEBUG)  # set the desired logging level here


@app.route("/")
def index():
    return "Welcome Heroku Flask!"


@app.route('/api/videos/process', methods=['POST'])
def videos_process():
    t0 = time.time()
    content = request.get_json(silent=True).get('content')
    #content = json.get('content')
    # app.logger.debug('A value for debugging')
    # app.logger.warning('A value for warning')
    # sys.stdout.write('Another message')
    # print(content.get('id').get('b'))
    #print(time.clock() - t0, "seconds wall time")

    result = video.process(content)
    # jsonify will do for us all the work, returning the
    # previous data structure in JSON
    # return jsonify(results = list)
    print(time.time() - t0, 'seconds', result, content)
    sys.stdout.flush()

    # return json.dumps(result)
    return jsonify({'caras': result})

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
