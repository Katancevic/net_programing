import socket

PORT = 35789

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect(("127.0.0.1", PORT))
print(f"[CLIENT] has recived from server: {client_socket.getsockname()}")

client_socket.sendall(bytes("Hi, there, server!", encoding = "utf8"))

reply = client_socket.recv(1024)
print(f"[CLIENT] response from the server {reply.decode('utf8')}")

client_socket.close()