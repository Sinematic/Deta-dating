import socket
import threading

host = '127.0.0.1'  # localhost
port = 65000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
pseudos = []


def broadcast(message):
    """fonction de diffusion"""
    for client in clients:

        client.send(message)


def handle(client):
    """fonction de gestion"""
    while True:
        try:
            message = client.recv(1024)  # .decode('UTF-8')
            # print(f"{pseudos[clients.index(client)]} dit : {message}")
            """print(clients)
            print(pseudos)"""
            broadcast(message)
        except:
            # si le client n'est plus la, ferme le client
            index = clients.index(client)
            clients.remove(client)
            client.close()
            pseudo = pseudos[index]
            broadcast(f'{pseudo}déconnecté...'.encode('UTF-8'))
            pseudos.remove(pseudo)
            break


def receive():
    """fonction de reception"""
    while True:
        # accepte le client tout le temps
        client, address = server.accept()
        # Envoie la confirmation de la connexion
        print(f"Connexion avec {str(address)}")
        # le client envoie son pseudo
        # client.send('ID'.encode('UTF-8'))
        # On reçoit le pseudo
        pseudo = client.recv(1024).decode('UTF-8')
        # on ajoute ce pseudo à notre liste de pseudos
        pseudos.append(pseudo)
        clients.append(client)

        # Renvoi de l'information
        print(f'Le pseudo est {pseudo}')
        # On annonce que untel a rejoint le chat
        # broadcast(f'{pseudo} vous êtes en ligne'.encode('UTF-8'))
        # On valide qu'il est connecté au serveur
        """client.send(f'Connecté au serveur'.encode('UTF-8'))"""
        # On veut un thread par client connecté
        thread = threading.Thread(target=handle, args=(client,))
        # le thread doit être demarré avec la méthode start et non run
        thread.start()


# On vérifie que le serveur est en écoute/enlever le cas échéant
print('serveur en écoute')
# On appelle la fonction
receive()
