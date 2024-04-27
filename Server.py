import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "127.0.0.1"
port = 12345
server_socket.bind((host, port))
server_socket.listen(1)
print("Serveur en attente de connexion...")
client_socket, client_address = server_socket.accept()
print("Connexion établie avec", client_address)
data = client_socket.recv(1024)
print("Message reçu du client:", data.decode())
response = "Message reçu. Merci!"
client_socket.send(response.encode())
client_socket.close()
server_socket.close()
