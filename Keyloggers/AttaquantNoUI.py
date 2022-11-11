import socket, logging

host = "192.168.1.7" # adresse du serveur (remplacer par l'ip)
port = 8888 # port d'écoute du serveur

file = "log.txt" # nom du fichier de logs 
logging.basicConfig(filename=file, level=logging.INFO, format="%(asctime)s %(message)s") # configuration du logger


with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock: # ouverture du soclet UDP
    sock.bind((host, port)) # écoute du port du serveur


    if sock:
        print("Socket créé !\r\nEn attente d'événements...")

        while True: # boucle infinie pour écouter les données entrantes
            d = sock.recvfrom(1024) # réception des données.
            data = d[0].decode('utf-8') # décodage du message reçu en utf-8
            addr = d[1] # adresse du client (non utilisée ici)

            if data: # si le message n'est pas vide
                logging.info(data) # on écrit le message dans le fichier de logs
                print(f"Reçu: {data}") # on affiche le message dans la console
