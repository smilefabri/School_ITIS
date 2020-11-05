import socket


print("avvio del server...")

with socket.socket(socket.AF_INET,socket.SOCK_DGRAM) as s:
    s.bind(("127.0.0.1",5006))
    
    while True:
        
        data, addr = s.recvfrom(8192)
        s.settimeout(20000)
        

        #log debug
        print(f"hai ricevuto il messaggio: {data.decode()}, da: {addr} ")
        data_lab = eval(data.decode())
        #rinvio il messaggio echo
        s.sendto(str(data_lab).encode("ascii"),addr)

