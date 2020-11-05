matrix = [[True, True, True, True, True, False],
    [False, False, True, True, True, False],
    [True, True, True, False, True, True],
    [True, False, False, True, True, False],
    [True, False, True, True, False, True], 
    [True, False, True, True, True, False]]

def controllo(Element) -> bool:
    if Element == True:
        return True
    else:
        return False

def bool_to_int(matrix)-> list:
    n_Node = 1
    temp_matrix = []
    for x in matrix:
        path_dict = []
        for y in x:
            if(controllo(y)== True):
                path_dict.append(n_Node)
                n_Node+=1
            else:
                path_dict.append(-1)
        temp_matrix.append(path_dict)
    
    return temp_matrix

def Search_path(matrix)-> dict:
    matrix = bool_to_int(matrix)
    final_dict = {}
    c = 0
    for x in range(len(matrix)-1):
        
        for y in range(len(matrix)-1):
            boh = []
            if  matrix[x][y] > 0:
                if matrix[x+1][y] > 0:
                    boh.append(matrix[x+1][y])
                if matrix[x-1][y] > 0:
                    boh.append(matrix[x-1][y])
                if matrix[x][y+1] > 0 :
                    boh.append(matrix[x][y+1])
                if matrix[x][y-1] > 0:
                    boh.append(matrix[x][y-1])
                    
            final_dict[matrix[x][y]] = boh
            #boh.clear()
            c = c+1


    return final_dict



def main():
    final = Search_path(matrix)



if __name__ == "__main__":
    main()
