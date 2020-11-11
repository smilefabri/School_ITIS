def scomp(n):
    dict_primi = {}
    fatt_primi = []
    c = 2
    while n >=  c:
        if n % c == 0:
            fatt_primi.append(c)
            n /=  c
        else:
            c += 1
    
    prec = 0
    for i in fatt_primi:
        
        if i != prec:
            u = fatt_primi.count(i)
            dict_primi[str(i)] = u
        prec = i
            
    return fatt_primi, dict_primi
            
                
             
        
        
if __name__ == "__main__":
    print(scomp(27000))
    