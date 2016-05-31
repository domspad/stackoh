from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

@app.route("/")
def hello():
    return render_template("index.html")

@socketio.on("tags_request")
def tags_request(message):
    print "Received tags_request: ", message

    # Call into SO API
    data = dict()
    data["test_tag"] = 1234

    socketio.emit("tags_data", data)

if __name__ == "__main__":
    import os

    socketio.run(app, host=os.environ['IP'], port=int(os.environ['PORT']), debug=True)
