import socket

ip = "192.168.1.53"
port = 4444

def main():
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    address = (ip,port)
    sock.bind(address)
    sock.listen(1)
    print("Connexion réussie au port "+ str(port))
    conn , ipvictime =  sock.accept()
    msg = "Message du serveur"
    conn.send(msg.encode())


    conn.close() 


instance ="ON"
while instance== "ON":
    main()