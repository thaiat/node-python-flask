import os
import sys
from flask import Flask, request, jsonify
import json
import logging
import video
import datetime
app = Flask(__name__)
app.logger.setLevel(logging.DEBUG)  # set the desired logging level here


@app.route("/")
def index():
    return "Welcome Heroku Flask!"


@app.route('/api/videos/process', methods=['POST'])
def videos_process():
    start = datetime.datetime.now()
    content = request.get_json(silent=True).get('content')
    # content = json.get('content')
    # app.logger.debug('A value for debugging')
    # app.logger.warning('A value for warning')
    # sys.stdout.write('Another message')
    # print(content.get('id').get('b'))
    # print(time.clock() - t0, "seconds wall time")

    caras = video.process(content)
    # caras = [{'y': 161, 'x': 83, 'height': 279, 'width': 210}]
    # jsonify will do for us all the work, returning the
    # previous data structure in JSON
    # return jsonify(results = list)
    # print((time.time() - t0).total_seconds(), 'seconds', caras)
    print("[INFO] Detection: {0}s, {1}".format(
        (datetime.datetime.now() - start).total_seconds(), caras))
    sys.stdout.flush()

    # return json.dumps(result)
    retval = jsonify({'results': {'caras': caras}})
    return retval

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
