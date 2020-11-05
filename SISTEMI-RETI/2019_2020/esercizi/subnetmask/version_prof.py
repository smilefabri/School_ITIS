import subprocess


ipaddress = "192.160.10.0"
mask = 20

ipaddress_splitted = [int(i) for i in ipaddress.split(".")]

ipaddress_bin = 0
for e, group in enumerate(ipaddress_splitted):
    ipaddress_bin = ipaddress_bin + group*(2**(((3-e)*8)))

lista_host = []
ipaddress_host = ipaddress_bin
for c in range(1,2**(32-mask)-1):
    ipaddress_host = ipaddress_host + 1
    l = '.'.join([str(int(bin(ipaddress_host)[i:i+8],2)) for i in range(2,34,8)])
    lista_host.append(l)

for i in lista_host:
    p = subprocess.Popen(['ping',i], stdout=subprocess.PIPE)
    ping = p.communicate()
    with open("log.txt","w") as c:
        print(ping[0].decode())
        c.write(ping[0].decode())