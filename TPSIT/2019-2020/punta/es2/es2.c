
#include<stdio.h>
#include<stdio.h>

main(){
    //creo le variabile per il funzionamento del mio programma
    int* v;//vettore dinamico
    int dim;// la dimensione del mio vettore
    int max; // variabile d'appoggio

    //l'utente inserisce la dimensione del vettore
    printf("inserire la dimesione:\n");
    scanf("%d" , &dim);

    //creo (alloco) l'area di memoria per il mio vettore
    v = (int*) malloc(dim*sizeof(int));

    //inserisco i valori al interno delle celle di memoria
    for (int k = 0; k < dim; k++){
        printf("v[%d] -> " , k);
        scanf("%d" , v+k);
    }

    max = *v;//imposto il valore più alto che sia uguale al primo elemento dell'array
    
    //cerco il massimo valore confrontando ogni valore con quello precendete ì, ma utilizzando i puntatori
    for(int i = 1; i<dim; i++){
        if(*(v+i)>max) max = *(v+i);
    }
    //stampo il più grande
    printf("final max = %d" , max);


    //free(v)
    getch();
    fflush(stdin);
}