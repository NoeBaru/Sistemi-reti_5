import socket

def main():
    """
    Author: Noemi Baruffolo
    date: 13/09/2024
    Descrizione: Ripasso liste, for, enumerate
    """
    versioni = ["4o", "40-mini", "o1-preview", "01-mini"]
    nomi = ["Noemi", "Danilo", "Mattia", "Simone"]

    #c style, DA NON USARE!
    for i in range(len(versioni)):
        print("ChatGPT " + versioni[i])

    print()

    #Python style
    for versione in versioni:
        print(f"ChatGPT {versione}")
    
    print()

    for indice, versione in enumerate(versioni):
        print(f"La versione {indice+1} ChatGPT {versione}")

    print()

    for nome, versione in zip(nomi, versioni): #zip affianca le liste, il ciclo termina sulla lista più corta e non ti da errore
        print(f"{nome} usa ChatGPT {versione}")
    
    nomi.append("Karol")
    print(nomi)

    print()

    #indicizzazione
    print(nomi[0]) #primo nome
    print(nomi[-1]) #ultimo elemento
    print(nomi[-2]) #penultimo elemento

    #slicing
    print(nomi[0:2]) #da 0 (si può omettere) a 2(estremo destro escluso)
    print(nomi[0:-1]) #tutti eccetto l'ultimo
    print(nomi[-2:]) #stampa gli ultimi due elementi
    print(nomi[::2]) #stampa gli elementi pari partendo da 0 e arriva fino in fondo saltando due per volta

if __name__ == '__main__':
    main()
