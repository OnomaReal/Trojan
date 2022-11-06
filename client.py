import socket

ip = "192.168.1.53"
port = 4444
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)


try:
    sock.connect((ip, port))
    print("Client connecté!")

    donnees = "Test"
    donnees = donnees.encode("utf8")
    sock.sendall(donnees)
except ConnectionRefusedError:
    print("La connexion au serveur n'a pas pu se faire")
finally:
    sock.close()
