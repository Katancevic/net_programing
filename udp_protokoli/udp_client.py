# socet biblioteka je zaduzena za osnovne mrezne komunikacije u Python-u
import socket

server_port = 21060

client_socet = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

input_s = "Zdravo, server"

client_socet.sendto(bytes(input_s, encoding = "utf8"), ("127.0.0.1", server_port))

input_s_modified, address = client_socet.recvfrom(65335)

print(f"Client respone from server ({address}, {input_s_modified.decode('utf8')})")
client_socet.close()

