import socketio
import eventlet

sio_server = socketio.Server()

app = socketio.WSGIApp(sio_server)

def connect(sid, headers):
    print("Client connected: ", sid)
@sio_server.event
def my_message(sid, data):
    print(f"User: {data['name']}, sent message: {data['msg']}")

eventlet.wsgi.server(eventlet.listen(('localhost', 5000)), app)
