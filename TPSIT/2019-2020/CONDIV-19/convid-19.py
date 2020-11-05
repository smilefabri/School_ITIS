from time import time
def print_Matrix(Matrix_node,Nodes):
    print("la matrice é:")
    for i in range(Nodes) :  
        for j in range(Nodes):
            print(Matrix_node[i][j], end=" ")
        print()

def Dict_node()->dict:
    with open("data.txt","r") as x:
        val = x.read()
        f = val.split("\n")

    dict_con = {}

    for g in range(0,200):
        contaggiati = f[g].split(" ")
        list_con = []
        for n in contaggiati[1:]:
            list_con.append(n)
        dict_con[str(contaggiati[0])] = list_con
    
    return dict_con

def dict_to_matrix(f)->list:
    Matrix_node = [[0 for i in range(0,200)] for j in range(0,200)]
    for x in f.keys() :
        for y in f[x]:
            Matrix_node[int(x)][int(y)] = int(y)

    return Matrix_node

def first_con(matrice):
    finish = []
    for y in range(1,200):
            test =[row[y] for row in matrice]
            if(sum(test)==0):
                finish.append(y)
    
    return finish
   
def main():
    start_time = time()
    ditc_no=Dict_node()
    matrix = dict_to_matrix(ditc_no)
    print(f"i pazienti 0 sono: {first_con(matrix)}")
    print("finito in :"+str(time()-start_time) )

if __name__ == "__main__":
    main()