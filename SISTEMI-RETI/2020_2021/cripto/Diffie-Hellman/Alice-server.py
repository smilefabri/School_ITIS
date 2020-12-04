import socket
import config



HOST = '127.0.0.1'  
PORT = 8500   

def calc_Key()->int:
    a = int(input(f"scegli un numero compreso tra 1 e {str(config.N)}: "))
    return pow(config.g,a,config.N),a
    

def Ini_com(conn):
    key,a = calc_Key()
    conn.sendall(str(key).encode())
    B = conn.recv(1024)
    return  pow(int(B.decode()),a,config.N)



def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        print("avvio server...")
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            data = conn.recv(1024)
            print(f"la mia chiave é: {Ini_com(conn)}")
            
                


if __name__ == "__main__":
    main()