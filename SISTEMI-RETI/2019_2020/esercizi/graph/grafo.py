Nodes = int(input("inserire il numero di nodi: "))
#ho trovato questo metodo veloce per creare matrici su www.geekforgeek.com
#x = [[elementi for x in range(colonne)]for j in range(righe)]
# od oppure c'è questo metodo  x = [[elementi]*colonne]*righe

Matrix_node = [ [ 0 for i in range(Nodes) ] for j in range(Nodes) ]

#è giusto però controlla cosa inserisci in input (non orientato)
print(Matrix_node)

for i in range(Nodes):
    Link = input(f"il nodo {i} a chi è collegato?: ").split(",")
    #peso = input(f"quanto il peso ").split(",")
    int_Link = [int (i) for i in Link]
    #int_peso = [int(i)fro i in peso]
    print(Link)
    for a in int_Link:
        if(i == a):
            Matrix_node[i][a] = 0
        else:
            Matrix_node[i][a] = 1 #peso[i]
     
print("la matrice é:")
for i in range(Nodes) :  
    for j in range(Nodes):
        print(Matrix_node[i][j], end=" ")
    print()

dict_Matrix = {}

#dizionario 
for i in range(Nodes):
    app_List = []
    for j in range(Nodes):
        if Matrix_node[i][j] == 1:
            app_List.append(str(j))
    dict_Matrix[i] = app_List
    
            

print(dict_Matrix)   