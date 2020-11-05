from sys import argv
import time
# read the WYSS section for how to run this
"""
un possibile errore durante la compilazione è quella di non soddisfare 
il numero di argomenti inseriti all'interno del codice 

ad esempio quando metti solo due argomenti invece di quelli prestabiliti che sono 4
esce un messaggio di errore.

"""
script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

# punto 3
nome = input("Nome: ")
print(f"lo script di nome: {script} è stato eseguito il giorno: {time.asctime( time.localtime(time.time()) )} da {nome}")