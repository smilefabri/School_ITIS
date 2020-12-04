import socket
import config

HOST = '127.0.0.1'  
PORT = 8500        

def calc_Key():
    b = int(input(f"scegli un numero  tra 1 e {str(config.N)}: "))
    Key = pow(config.g,b,config.N)
    return Key,b

def Ini_com(conn)->int:
    key,b = calc_Key()
    A = conn.recv(1024)
    print(f"alice: {A.decode()}")
    conn.sendall(str(key).encode())
    K = pow(int(A.decode()),b,config.N)
    return K

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(b'Hello, world')
        Key_bob = Ini_com(s)
        #data = s.recv(1024)
        print(f"la mia chiave è: {Key_bob}")



if __name__ == "__main__":
    main()
        