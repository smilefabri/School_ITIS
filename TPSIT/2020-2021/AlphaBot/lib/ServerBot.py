import socket
from socket import error
import sqlite3
import threading


class ServerBot(threading.Thread):
    
    def __init__(self,ip = "0.0.0.0",port= 7000,sock=None) -> None:
        threading.Thread.__init__(self)
        self.__port_server = port
        self.__ip_server = ip
        #trasformarlo in un dizionario
        self.__List_client= []
        if sock is None: # l'espressione sock is None è uguale a dire sock == None (più o meno)
            self.__sock_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.__sock_server= sock
        
        print(f"server started with hostname: {self.__ip_server} and port: {self.__port_server}")
        print("-----------------------------------------------")
        try:
            #auto bind ahahha
            self.__sock_server.bind((self.__ip_server,self.__port_server))
        except socket.error as error:
            print(error)
             
    #zona gestione server
 
    def Accept(self):
        (client_sock, (ip,port)) = self.__sock_server.accept()
        return (client_sock, (ip,port)) 
    
    #ferma il il server
    def stop_server(self):
        #aggiungere anche la funzione che uccide il thead prima di close 
        self.__sock_server.close()
    
    def Listen(self,flag=None):
        if flag is None:
            self.__sock_server.listen()
        else:
            self.__sock_server.listen(flag)
            
    def Add_Client(self,ip,port,client_sock,DB_name):
        
        newClient = Client_Thread(ip,port, client_sock,DB_name)
        newClient.start()
        self.__List_client.append(newClient)
        
    #get and set
    def get_Client(self):
        return self.__List_client
    

class Client_Thread(threading.Thread):
    
    def __init__(self,ip,port,socket,DB_name):
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.conn = socket
        self.DB_name = DB_name
        print (f"[+] nuovo thread con ip:{self.ip} e con porta: {self.port}")
        
    def receive(self):
       buf = self.conn.recv(4096)
       return buf.decode()
    
    def Mysend(self,buf):
        self.conn.sendall(buf)
    
    def run(self):
        print("si è connesso:"+self.ip+" alla porta:"+str(self.port))
        
        # riceve una stringa che dovra essere divisa .split("-")
        while True:
            try:
                data = self.receive()
                dest= data.split(",")
                
                if len(dest) == 2:
                    print(f"from: {dest[0]}, to: {dest[1]}")
                    #inserire sql interogazioni
                    #se hai voglia ripulire l'input dell'utente
                    with sqlite3.connect(self.DB_name) as connsql:
                        c = connsql.cursor()
                        #print(f'Query: SELECT id FROM luoghi WHERE nome="{data[0]}"')
                        for row in c.execute(f"SELECT percorso FROM Luoghi WHERE Start_point = {dest[0]} AND end_point= {dest[1]} "):
                            self.percorso = row[0]
                            
                            
                        self.Mysend(self.percorso.encode())
                else:
                    self.Mysend(b"hai sbagliato!(from-to)")
                    
                if data == "close":
                    self.conn.close()
                    
            except socket.error as msg:
                print(msg)
                break
                   
            #self.conn.close()
        
