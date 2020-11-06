from lib.ServerBot import ServerBot


def main():
    Server_bot = ServerBot("192.168.1.126",7500)
    
    
    while True:
        Server_bot.Listen()
        (clientsock, (ip,port))= Server_bot.Accept()
        Server_bot.Add_Client(ip,port, clientsock)
        
        print(Server_bot.get_Client())
        
        
 #   print("debug")



if __name__ == "__main__":
    main()
