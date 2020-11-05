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

def encrypt(message, key):
    message = list(message)
    baseNum = []
    criptato = []
    key = key.split("-")
    key = [int(c) for c in key]
    
    for x in message:
        for y in alfabeto:
            if x == y:
                baseNum.append(alfabeto[y])
    
    for x in range(0,len(baseNum)):
        for keys,values in alfabeto.items():
            temp = (baseNum[x]+key[x])% 26
            if  temp == values:
                criptato.append(keys)
                
    return "".join(criptato)

def decrypt(message,key):
    message = list(message)
    baseNum = []
    criptato = []
    key = key.split("-")
    key = [int(c) for c in key]
    
    for x in message:
        for y in alfabeto:
            if x == y:
                baseNum.append(alfabeto[y])
    
    for x in range(0,len(baseNum)):
        for keys,values in alfabeto.items():
            temp = (baseNum[x]-key[x])% 26
            if  temp == values:
                criptato.append(keys)
            
            
    return "".join(criptato)
    
    

if __name__ == "__main__":
    message = "COME STAI?"
    key = "8-17-8-16-3-4-9-13-12-20-20-12"
    
    message = encrypt(message, key)
    print(message)
    
    print(decrypt(message,key))
    
    