def gamering(naam, leeftijd):
    print("Hallo, " + naam + " uw leeftijd is " + leeftijd + " jaar.")

def start():
    naam = input("Wat is uw naam? ")
    leeftijd = input("Hoe oud bent u? ")
    gamering(naam,leeftijd)
    start()

if start() == True:
    start()