from flask import Flask, render_template, request
from flask_socketio import SocketIO

from data_utils import tag_question_count

app = Flask(__name__)
socketio = SocketIO(app)

clients = list()

@app.route("/")
def hello():
    return render_template("index.html")

@socketio.on("connect")
def client_connect():
    print "New connection: ", request.sid
    clients.append(request.sid)

@socketio.on("disconnect")
def client_disconnect():
    print "Disconnect: ", request.sid
    clients.remove(request.sid)

@socketio.on("tags_request")
def tags_request(message):
    print "Received tags_request:", message

    tags = [s.strip() for s in message.split(",")]
    if len(tags) > 0:
        data = dict()
        for t in tags:
            data[t] = tag_question_count(t)

        socketio.emit("tags_data", data, room=request.sid)

if __name__ == "__main__":
    import os

    socketio.run(app, host=os.environ['IP'], port=int(os.environ['PORT']), debug=True)
