'''
metodi utili per risolvere il problema

.zfill(arg) ti aggiunge degli zeri fino ad arrivare una lunghezza uguale ad arg 
.join() fa l'opposto di split, invece di dividere unisce tutti gli elementi al interno di una lista
.split(arg) prede una stringa e lo divide ogni volta che trova un carattere unguale all'argomento
.count(arg) conta gli elementi all'intero di un valore compatibile
[int(i) for i in mask] metodo veloce per fare un ciclo
'''


#funzioni per pigrizia
def Controll_ip(Int_ip):
    cond = True
    while cond:
        if(len(Int_ip) == 4) and (Int_ip[0]<=255 and Int_ip[0]>=0)and(Int_ip[1]<=255 and Int_ip[1]>=0)and(Int_ip[2]<=255 and Int_ip[2]>=0)and(Int_ip[3]<=255 and Int_ip[3]>=0):
            cond = False
        else:
            print("invalid IP...")

def Convert_bin(Lista):
    return [format(i,'#010b') for i in Lista]

def Convert_str(Lista):
    return [str(i) for i in Lista]

def Calcolo_rete(Ip,mask):
    Lista_appoggio = [0,0,0,0]
    for i in range(0,4):
        Lista_appoggio[i] =  Ip[i] & mask[i]

    return Lista_appoggio

def N_host(bit_list):
    pass
#converto l'ip in binario e faccio eventuali controlli

ip = input("inserire l'indirizzo ip: ").split(".")
mask = input("inserire la mask con la not notation(255.255.255)").split(".")

Int_ip = [int(i) for i in ip]
Int_mask = [int(i) for i in mask]


Calcolo_rete = Calcolo_rete(Int_ip,Int_mask)


x = ".".join(Convert_str(Calcolo_rete))
print(f"la tua rete è: {x}")








