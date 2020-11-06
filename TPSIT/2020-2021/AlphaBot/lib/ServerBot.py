import socket
from socket import error
#import sqlite3
import threading


class ServerBot(threading.Thread):
    
    def __init__(self,ip = "0.0.0.0",port= 7000,sock=None) -> None:
        threading.Thread.__init__(self)
        self.__port_server = port
        self.__ip_server = ip
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
            
    def Add_Client(self,ip,port,client_sock):
        
        newClient = Client_Thread(ip,port, client_sock)
        newClient.start()
        self.__List_client.append(newClient)
        
    #get and set
    def get_Client(self):
        return self.__List_client
    

class Client_Thread(threading.Thread):
    
    def __init__(self,ip,port,socket):
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.conn = socket
        print (f"[+] nuovo thread con ip:{self.ip} e con porta: {self.port}")
        
    def receive(self):
       return self.conn.recv(4096)
    
    def Mysend(self,buf):
        self.conn.sendall(buf)
    
    def run(self):
        print("si è connesso:"+self.ip+" alla porta:"+str(self.port))
        while True:
            try:
                buf = self.receive()
                print(buf.decode())
                self.Mysend(buf)
                if buf == "close":
                    self.conn.close()
            except:
                pass
        
