import os
from flask import Flask, request, jsonify
import json
app = Flask(__name__)


@app.route("/")
def index():
    return "Welcome Heroku Flask!"


@app.route('/api/videos/process', methods=['POST'])
def videos_process():
    content = request.get_json(silent=True)
    print(content.get('id').get('b'))
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
