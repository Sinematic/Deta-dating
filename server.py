import socket

# host = ''  # localhost
# port = ''

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 9999))
server.listen()


client, addr = server.accept()


done = False

while not done:
    msg = client.recv(1024).decode('UTF-8')
    if msg == 'quit':
        done = True
        print("Client disconnected")
    else:
        print(f'Exppéditeur : {msg}')
    client.send(input("Vous: ").encode('UTF-8'))

client.close()
server.close()
