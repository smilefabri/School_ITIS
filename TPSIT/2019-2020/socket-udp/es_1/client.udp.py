import socket

with socket.socket(socket.AF_INET,socket.SOCK_DGRAM) as s:
    stringa: str = "hello world"
    s.sendto(stringa.encode("ascii"), ("localhost", 5000))
    dati = s.recv(8192)
    print("eco del messaggio dal server: " + dati.decode("ascii"))



