import threading
import socket

host = "127.0.0.1" # localhost
port = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
nicknames = []

def broadcast(message):
    for client in clients:
        client.send(message)
        
def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except Exception:
            index = clients.index[client]
            client.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f'{nickname} left the chat!'.encode('ascii'))
            nicknames.remove(nickname)
            break

def receive():
    while True:
        client, address = server.accept()
        print(f"Connected with {address}")
        
        # Send code word
        client.send('NICK'.encode("ascii"))
        nickname = client.recv(1024).decode("ascii")
        nicknames.append(nickname)
        clients.append(client)

        # Achknowledge the connection
        print(f'Nickname of the client is: {nickname}')
        broadcast(f'{nickname} joined the chat!'.encode('ascii'))
        client.send('Connected to the server!'.encode('ascii'))
        
        # Start a thread to this client
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()
        
if __name__ == '__main__':
    print('The server is listening ...')
    receive()
    

