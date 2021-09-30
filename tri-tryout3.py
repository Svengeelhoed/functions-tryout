def gamering(naam, leeftijd):
    print("Hallo " + naam + ", uw leeftijd is " + leeftijd + " jaar.")

def start():
    naam = input("Wat is uw naam? ")
    if naam == "stop":
        exit()
    leeftijd = input("Hoe oud bent u? ")
    if leeftijd == "stop":
        exit()
    gamering(naam,leeftijd)
    start()

start()