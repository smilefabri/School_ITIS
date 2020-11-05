#include<stdio.h>
#include<stdio.h>
#include<string.h>

void main(){
    //creo le variabile che mi serviranno
    char* string;// creo la mia stringa, ma con il puntatore
    int length = 0;//metto la lunghezza prendefinita == 0


    //creo (alloco) l'area di memoria per la mia stringa
    string = (char*) malloc(50*sizeof(char));


    //faccio inserire la stringa da misurare
    printf("inserire la stringa: \n");
    gets(string);
    printf("stringa = %s" , string);//stampo a video

    //scorre tutta mia stringa finche non trova EOF che indica la fine della mia stringa
    while(*string!='\0'){
        length++;
        string++;//passa al prossimo carattere
    }

    printf("lunghezza = %d" , length);// stampa la lunghezza 

    //free(string)
    
    fflush(stdin);
    
}