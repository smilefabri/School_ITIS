#include<stdio.h>
#include<stdlib.h>
#include<string.h>
//creo una costante che sarà mia dimesione fissa == 50
#define DIM 50


//definisco la struttura
typedef struct structure
{
    char name[DIM];
    int number;
}Structure;


int main(){

    //
    Structure* list;
    int dim = 0;
    //faccio inserire la dimensione 
    printf("inserire la dimensione:\n");
    scanf("%d" , &dim);
    //creo (alloco) l'area di memoria per la mia struttura (lista)
    list = (Structure*) malloc(dim*sizeof(Structure));

    //Stampo la dimensione della struttura in bytes
    printf("dimensione della struttura (bytes)= %d\n" , sizeof(Structure));



    for (int i = 0; i < dim; i++){
        char temp[DIM];
        printf("%d = " , i);

        fflush(stdin);
        gets(temp);

        printf("\n");

        strcpy((i+list)->name, temp);

        (i+list)->number = i;
    }
    

    for (int k = 0; k < dim; k++){
        printf("lista[%d] = %p\n" , k , (list+k));
    }

    for (int i = 0; i < dim; i++)
    {
        printf("structure %d\n " , i);
        printf("name: %s \t number: %d" ,(list+i)->name , (list+i)->number );
        printf("\n");
    }
    

    
    free(list);

    getch();
    fflush(stdin);
    return 1;
}