from flask import Flask
from flask_cors import CORS
from flask_socketio import SocketIO, join_room

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="https://stephenfujiwara-chat-client.netlify.app")

@socketio.on("connect", namespace="/chat")
def handle_connection():
    print("someone has connected")

@socketio.on("disconnect", namespace="/chat")
def handle_disconnect():
    print("someone has disconnected")

@socketio.on("join_room", namespace="/chat")
def handle_join_room(data):
    join_room(data["room"])
    print(f"User {data['id']} has joined room {data['room']}")

@socketio.on("send_message", namespace="/chat")
def handle_send_message(data):
    socketio.emit("receive_message", data, namespace="/chat", to=data["room"])

if __name__ == "__main__":
    socketio.run(app, debug=True)