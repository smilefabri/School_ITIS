import socket

ip_server = "192.168.88.75"
port_server = 7000

def main():
    print("avvio...")
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client:

        while(True):
            msg = "hello world"
            client.sendto(msg.encode(),(ip_server,port_server))

            raw_data = client.recv(4096)

            print(">>" + raw_data.decode())



if __name__ == "main":
    main()