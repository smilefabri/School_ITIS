
#assegna alla variabile il valore 10
types_of_people = 10

# alla variabile x assegno la stringa formatata
x = f"There are {types_of_people} types of people."

# a binary assegno una stringa
binary = "binary"

# a do_not assegno una stringa
do_not = "don't"

# alla variabile y assegno una stringa formatata
y = f"Those who know {binary} and those who {do_not}."

# stampo la variabile x
print(x)
# stampo la variabile y
print(y)

# stampo usando stringa formattata che stampa x 
print(f"I said: {x}")
# stampo usando stringa formattata che stampa y 
print(f"I also said: '{y}'")

# assegno a hilarious False
hilarious = False
# assegno a joke_evaluation una stringa, da notare le graffe al fondo che servono per usare .format
joke_evaluation = "Isn't that joke so funny?! {}"

# stampo usando .format per inserire 
print(joke_evaluation.format(hilarious))

# a w assegno una stringa
w = "This is the left side of..."
# a e assegno una stringa
e = "a string with a right side."

# stampo w concatenata a e
print(w + e)