from flask import Flask, render_template, request
from flask_socketio import SocketIO

from data_utils import tag_question_count

import websocket
from multiprocessing import Pool, TimeoutError

app = Flask(__name__)
socketio = SocketIO(app)

clients = list()

#ws = websocket.create_connection("ws://qa.sockets.stackexchange.com/")
#ws.send("155-questions-active")

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

        print "Sending tags_data"
        socketio.emit("tags_data", data, room=request.sid)

def wait_and_do_magic():
    print "Start the magic!"
    import time
    time.sleep(3)
    return str(time.time())
    #return ws.recv()

def magic_callback(str_data):
    print "Sending update to clients!", str_data
    socketio.emit("so_update", str_data, broadcast=True)
    print "Successfully emitted data!"
    pool.apply_async(wait_and_do_magic, callback=magic_callback)

pool = Pool()

#@app.before_first_request
#def start_magic():
#    pool.apply_async(wait_and_do_magic, callback=magic_callback)

if __name__ == "__main__":
    import os

    pool.apply_async(wait_and_do_magic, callback=magic_callback)
    socketio.run(app)#, host=os.environ['IP'], port=int(os.environ['PORT']))#, debug=True)
