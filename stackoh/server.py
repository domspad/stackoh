from flask import Flask, render_template
from flask_socketio import SocketIO

from data_utils import get_tag_info

app = Flask(__name__)
socketio = SocketIO(app)

@app.route("/")
def hello():
    return render_template("index.html")

@socketio.on("tags_request")
def tags_request(message):
    print "Received tags_request:", message

    tags = [s.strip() for s in message.split(",")]

    data = dict()
    for t in tags:
        data[t] = get_tag_info(t)

    socketio.emit("tags_data", data)

if __name__ == "__main__":
    import os

    socketio.run(app, host=os.environ['IP'], port=int(os.environ['PORT']), debug=True)
