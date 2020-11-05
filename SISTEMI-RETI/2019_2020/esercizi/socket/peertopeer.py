import socket

ip_mio = '192.168.0.120'
port = 7000
ip_server = '192.168.0.112'
buf=0


def recever():
    global buf
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ip_mio,port))
    server.listen()
    while True:
        conn, addr = server.accept()
        print("connected by",addr)
        buf = conn.recv(4096)
        if not buf:
            print(buf.decode())
            break
        conn.sendall(buf)
        
    server.close()
        
    
def sender():
    global buf
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    client.connect((ip_server,port))
    
    
    client.sendall(buf)
    
    data = client.recv(4096)
    if not data:
        print(data)
    client.close()


if __name__ == "__main__":
    recever()
    sender()
    

