import networkx as nx


def Non_ori(Nodes):
    
    Matrix_node = [ [ 0 for i in range(Nodes) ] for j in range(Nodes) ]

    for i in range(Nodes):
        Link = input(f"il nodo {i} a chi è collegato?: ").split(",")
        int_Link = [int (i) for i in Link]
        
        for a in int_Link:
            if(i == a):
                Matrix_node[i][a] = 0
            else:
                Matrix_node[i][a] = 1
    return Matrix_node

def Non_ori_pesato(Nodes):
    
    Matrix_node = [ [ 0 for i in range(Nodes) ] for j in range(Nodes) ]
    for i in range(Nodes):
        link = input(f"a chi è collegato {i}?: ").split(",")
        int_Link = [int (i) for i in link]
        
        for a in int_Link:
            Matrix_node[i][a] = input(f"quanto pesa il link tra {i}:{a}: ")
    return Matrix_node    
     
def fromList_toDict(Matrix_node,Nodes):
    dict_Matrix = {}
    #dizionario 
    for i in range(Nodes):
        app_List = []
        for j in range(Nodes):
            if Matrix_node[i][j] == 1:
                app_List.append(str(j))
        dict_Matrix[i] = app_List
    return dict_Matrix

def fromListpes_toDict(Matrix_node,Nodes):
    List_to_dict = {} 

    for riga in range(Nodes):
        List_to_dict[riga] = {} 
        for colonna in range(Nodes):
            List_to_dict[str(riga)][str(colonna)] = str(Matrix_node[riga][colonna])

    return List_to_dict

def print_Matrix(Matrix_node,Nodes):
    print("la matrice é:")
    for i in range(Nodes) :  
        for j in range(Nodes):
            print(Matrix_node[i][j], end=" ")
        print()


#data visual.

def Network_Matrix(Matrix_node,Nodes):
    pass

def main():
    pass

if __name__ == "__main__":
    main()
