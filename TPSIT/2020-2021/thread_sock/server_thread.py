import socket
import threading

class ClientThread(threading.Thread):

    def __init__(self,ip,port,socket):
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.conn = socket
        print ("[+] nuovo thread "+ip+" :"+str(port))

    def run(self):
        print("si è connesso:"+self.ip+" alla porta:"+str(self.port))
        while True:
            try:
                buf = self.conn.recv(4096)
                print(buf.decode())
                self.conn.sendall(buf)
                if buf == "close":
                    self.conn.close()
            except:
                pass

     
     
def controllo():
    pass


def main():

   

    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
    sock.bind(("Localhost",7000))
    
    tasto = threading.Thread(target=controllo)   
    tasto.start() 
    
    cond = True
    while cond:
        sock.listen()
        (clientsock, (ip,port))= sock.accept()
        newClient = ClientThread(ip,port, clientsock)
        newClient.start()
        list_conn.append(newClient)
        
        
    
        
if __name__ == "__main__":
    list_conn = []
    main()
        