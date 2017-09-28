

quotes = [ 
        "Ecoutez-moi, Monsieur Shakespeare, nous avons beau etre ou ne pas etre, nous sommes !",
        "On doit pouvoir chosiir entre s'écouter parler et se faire entendre." ]

characters = [ 
        "alvin et les Chipmunks",
        "Babar",
        "betty boop",
        "calimero",
        "casper",
        "le chat potté"
        "Kirikou"]

if user_answer == "B":
    pass
elif user_answer == "C":
    print("C pas la bonne réponse ! Et G pas d'humour, je C..")

else:

    #show another quote 

def show_random_item(my_list):

    #TODO: get a random number

    item = my_list[0] #get a quote from a list

    print(item) # show the quote in the interpreter 

    return "program is over" # returned value 

print(show_random_item(quotes))


