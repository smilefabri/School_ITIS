/*crea una lista e la stampa*/
#include <stdio.h>
#include <stdlib.h>

struct El
{
    int valore;
    struct El* next;
};

void stampaLista(struct El* ListaDiElementi, int * e)
{
    if(ListaDiElementi==NULL) return;
    else
    {
        printf("%d - %p \n",ListaDiElementi->valore, ListaDiElementi->next);
        ListaDiElementi=ListaDiElementi->next;
        *e = *e + 1;
        stampaLista(ListaDiElementi, e);
    }
}

int main()
{
    int elementi = 0;    //numero di elementi nella lista
    int n;
    struct El* lista;
    struct El* l;
    lista=NULL; /* inizializzo a NULL, primo elemenot della lista */

    do
    {
        printf("Inserisci un naturale oppure -1 per terminare\n");
        scanf("%d",&n);

        if (n>=0)
        {
            if (lista==NULL) /* controllo se esiste solo una struttura */
            {
                /* alloco lo spazio per una struttura */
                lista = (struct El*) malloc(sizeof(struct El));
                l = lista;
            }
            else /* se il puntatore lista è diverso da NULL*/
            {
                /*assegno al puntatore l dell'elemento corrente un puntatore che punta all'elemento successivo*/
                l->next = (struct El*) malloc(sizeof(struct El));
                l = l->next;
            }

            l->valore = n; /* assegno n al campo dell'elemento corrente*/
            l->next = NULL; /* assegno al campo next dell'elemento corrente NULL */
        }
    } while (n>=0);

    l=lista; /* assegno alla variabile di appoggio l il puntatore al primo elemento della lista */
    

    stampaLista(l,&elementi);

    printf("elementi della lista = %d" , elementi);

    printf("\n");
    return 0;
 }