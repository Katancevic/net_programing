import socket, sys

PORT = 35789

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("127.0.0.1", PORT))
server_socket.listen(1)
while True:
    print(f"[TCP SERVER] Listening at: {server_socket.getsockname()}")

    conn_socket, conn_sockname = server_socket.accept()
    print(f"[TCP SERVER] Conection is accepted from: {conn_sockname}")
    print(f"[TCP SERVER] Socket connects: server_socket: {conn_socket.getsockname()}, and conn_socket: {conn_socket.getpeername()}")
    message = conn_socket.recv(1024)
    print(f"[TCP SERVER] The client_socket at: {conn_socket.getpeername()}, orginaly sent: {message.decode('utf8')}")
    modified_mesage = str(len(str(message).split(",")))

    conn_socket.sendall(bytes(modified_mesage, encoding = "utf8"))   
    conn_socket.close()
    print("[CLIENT] Replay sent, closing client's socket")
server_socket.close()


