import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("localhost", 9999))

done = False

while not done:
    client.send(input("Vous: ").encode('UTF-8'))
    msg = client.recv(1024).decode('UTF-8')
    if msg == 'quit':
        done = True
        print("Vous êtes déconnecté")
    else:
        print(f'Destinataire : {msg}')

client.close()
