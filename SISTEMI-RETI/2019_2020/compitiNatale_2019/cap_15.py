#importo il modulo sys
from sys import argv
#conservo il valore all'interno di argv in due variabili(disolito conserva gli argomenti che l'utente inserisce da linea di commando)
script, filename = argv
#apro il file con la funzione open(nome file)
txt = open(filename)
#stampo a video il nome del file che ho aperto 
print(f"Here's your file {filename}:")
#poi stampo a video il contenuto del file selezionato
print(txt.read())
#chiudo il file va sempre usato, per sicurezza usare il metodo with
txt.close()

