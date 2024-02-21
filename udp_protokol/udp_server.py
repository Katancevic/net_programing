import socket

server_port = 21060

server_seocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_seocket.bind(('127.0.0.1', server_port))
print("Server is started")

while True:
    message, address = server_seocket.recvfrom(63535)
    modified_message = str(len(str(message).split(",")))
    print(f"SERVER: ({modified_message})")
    server_seocket.sendto(bytes('Server is sending {}'.format(modified_message), encoding = 'utf8') , address)
server_seocket.close()