""" 
    pubblici:
    n,c

    privati:
    p,q,m e d

    TEST:
    -n: 536131
    -c: 5939
    [459541, 134033, 243696, 243696, 497836, 121848, 497836, 252297, 243696, 357421]

 """
import random

alfabeto = {
    "A":0,
    "B":1,
    "C":2,
    "D":3,
    "E":4,
    "F":5,
    "G":6,
    "H":7,
    "I":8,
    "L":9,
    "M":10,
    "N":11,
    "O":12,
    "P":13,
    "Q":14,
    "R":15,
    "S":16,
    "T":17,
    "U":18,
    "V":19,
    "Z":20,
    "?":21,  
    " ":23,
    ".":24,
    "!":25
}

def Is_prime(n):
    #n=int(input("Inserire un numero: "))
    if n<=1:
        print("Devi inserire un numero maggiore di 1")

    else:
        d,count=2,0
        while d<=n/2 and count==0:
            if n%d==0:
                count+=1
            d+=1
        if count==0:
            return True
        else:
            return False

def MCD(a,b):
    while b != 0 :
        r = a % b
        a = b
        b = r 
    #print(a)
    return a

def mcm(a,b):
    if a != "" and b != "":
        c = a*b/MCD(a,b)
    else:
        c = False
    return c

def key_p(m):
    c=2
    d=0
    while True:
        if 1 < c and c < m:
            if MCD(c,m) == 1:
                break
            else:
                c+=1
    else:
        print("hai sbagliato qualcosa!")

    while True:
        if 0 <= d and d < m:
            if (37*d)%m == 1:
                break
            else:
                d+=1
        else:
            print("non va bene....")
    
    return (c,d)
            
def encrypt(n,c,a):
    
    b = pow(a,c) % n

    return b 
        
def convert_text(char2number):
    number2char = []
    for i in range (65,91):
        char2number[chr(i)] = i - 65
        number2char[i-65] = chr(i)

    

if __name__ == "__main__":
    pas= ["C","O","G","L","I","O","N","E"]
    p =  17
    q =  11
    #convert_text(pas)
    if Is_prime(p) and Is_prime(q):
        n= p*q
        m = int(mcm(p-
        1,q-1))
        c,d = key_p(m)
        #print(encrypt(n,c,convert_text(pas)))

    else:
        print("error")

    print(f""" 
        PRIVATE:
            p={p}
            q={q}
            m={m}
            d={d}
        PUBBLICHE:
            n={n}
            c={c}
    """)