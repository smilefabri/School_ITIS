
def Non_ori_pesato(Nodes):
    
    Matrix_node = [ [ 0 for i in range(Nodes) ] for j in range(Nodes) ]
    for i in range(Nodes):
        link = input(f"a chi è collegato {i}?: ").split(",")
        int_Link = [int (i) for i in link]
        
        for a in int_Link:
            Matrix_node[i][a] = input(f"quanto pesa il link tra {i}:{a}: ")
    return Matrix_node 

    
def fromListpes_toDict(Matrix_node,Nodes):
    Matrix_dict = {}
    for node in range(Nodes):
        for LinkNodes in range(Nodes):
            Matrix_dict[node] = {LinkNodes:Matrix_node[node][LinkNodes]}
    return Matrix_dict


if __name__ == "__main__":
    Nodes = int(input("inserire il numero di nodi: "))
    matrix = Non_ori_pesato(Nodes)
    d = fromListpes_toDict(matrix,Nodes)



