import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "127.0.0.1"
port = 12345
client_socket.connect((host, port))
message = "Bonjour, serveur!"
client_socket.send(message.encode())
response = client_socket.recv(1024)

print("Réponse du serveur:", response.decode())
client_socket.close()
