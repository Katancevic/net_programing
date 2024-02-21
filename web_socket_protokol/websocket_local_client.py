import socketio

username = input("Your username is: ")
sio_client = socketio.Client()

def send_msg():
    while True:
        msg = input("Enter message: ")
        sio_client.emit('my_message', {'msg': msg, 'name': username})
sio_client.sleep(1)


@sio_client.event
def connect():
    print("Connection established")
    send_msg()
sio_client.connect('http://localhost:5000')
sio_client.wait()
