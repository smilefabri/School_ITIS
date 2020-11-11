def MCD(a,b):
    while b != 0 :
        r = a % b
        a = b
        b = r 
    return a
            
    
if __name__ == "__main__":
    print(MCD(24,36))