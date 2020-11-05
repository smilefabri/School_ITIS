

#include<stdio.h>
#include<stdlib.h>

main(){
    int* v;//creo la variabile puntatore
    int dim;// variabile per chidere la dimensione


    //prendo la dimensionedall'utente
    printf("\nInsert the dimension of the int vector:\n");
    scanf("%d" , &dim);

    //creo l'area di memoria per il mio vettore
    v = (int*) malloc(dim*sizeof(int));


    //inserisco i valori al interno delle celle di memoria
    for (int k = 0; k < dim; k++){
        printf("v[%d] = " , k);
        scanf("%d" , v+k);
    }
    //stampo i valori a video
    for(int i = 0; i<dim; i++){
        printf("v[%d] = %d\n" , i, *(v+i));
    }


    // ci starebbe una free(v) 
    //ripulisco
    getch();
    fflush(stdin);
}