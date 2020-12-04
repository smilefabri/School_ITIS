import socket

server_ip = "127.0.0.1"
server_port = 7500

def client():
    c = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    c.connect((server_ip,server_port))
    c.sendall(b'ciao')
    while True:
        #se genera un errore invia un errore di calcolo al server
        try:
            msg = c.recv(4096)
            if msg.decode() == "exit":
                c.close()
                break
            print(msg.decode())
            risultato = eval(str(msg.decode()))
            print(risultato)
            c.sendall(str(risultato).encode())
        except:
            c.sendall(b"ERROR")
            


        
    
    c.close()


if __name__ == "__main__":
    client()