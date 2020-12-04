import socket
import threading
import sqlite3

class ClientThread(threading.Thread):
    """ 
    la classe client che gestisce i recv e send per il calcolo distribuito 
    
    """
    
    #costruttore
    def __init__(self,ip,port,socket,N,db):
        
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.conn = socket
        self.N = N
        self.db = db
        #print ("[+] nuovo thread "+ip+" :"+str(port))

    #main che gestisce il thread
    def run(self):
        #print("si è connesso:"+self.ip+" alla porta:"+str(self.port))
        
        try:
            buf = self.conn.recv(4096)
            #print(buf.decode())
            for i in self.db:
                if i == str(self.N+1):
                    for j in database[i]:
                        self.conn.sendall(j.encode())
                        buf = self.conn.recv(4096)
                        print (f"{j} = {buf.decode()} from {self.ip} - {self.port}") 
        
            
            self.conn.sendall(b'exit')
                


        except:
            pass


def Load_db():
    """
        mi collego a un database e carico tutti i dati all'interno di un dizionario

        db = {
            "numero_cliente": [lista_di_valori]
            },
            etc..
    
    """
    db ={
        "1":[],
        "2":[]

    }
    with sqlite3.connect("C:/Users/fabri/Documents/GitHub/School_ITIS/TPSIT/2020-2021/verfiche/verifica_20_11/operations.db") as connsql:
        c = connsql.cursor()
            #print(f'Query: SELECT id FROM luoghi WHERE nome="{data[0]}"')
        for row in c.execute("SELECT client,operation FROM operations"):
            if row[0] == 1:
                db[str(row[0])].append(row[1])
            elif row[0] == 2:
                db[str(row[0])].append(row[1])
        #print(db)
        return db


def main():
    """ 
    
    funziona principale che avvia il server 
    """

    global database
    #caricamento database
    database = Load_db()
    #contatore clienti
    N_cli = 0
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
    sock.bind(("Localhost",7500))
    
    
    cond = True
    while cond:
        #server in ascolto
        sock.listen()
        #un client si collega
        (clientsock, (ip,port))= sock.accept()
        #creazione di cleinte 
        newClient = ClientThread(ip,port, clientsock,N_cli,database)
        newClient.start()
        #aggiunge il client a una lista
        list_conn.append(newClient)
        #incremento del contatore clienti
        N_cli +=1

if __name__ == "__main__":

    database = {}
    #lista connessioni
    list_conn = []
    main()
    