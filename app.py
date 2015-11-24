import os
from flask import Flask, request, jsonify
import logging
import video
import datetime


app = Flask(__name__)

stream_handler = logging.StreamHandler()
app.logger.addHandler(stream_handler)
app.logger.setLevel(logging.INFO)  # set the desired logging level here
app.logger.info('app started')


@app.route('/')
def index():
    return "Welcome Heroku Flask!"


@app.route('/api/videos/process', methods=['POST'])
def videos_process():
    start = datetime.datetime.now()
    jsonBody = request.get_json(silent=True)
    content = jsonBody.get('content')

    caras = video.process(content)

    app.logger.info('[INFO] Detection: {0}ms, {1}'.format(
        (datetime.datetime.now() - start).total_seconds()*100, caras))

    # return json.dumps(result)
    retval = jsonify({'results': {'caras': caras}})
    return retval

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
