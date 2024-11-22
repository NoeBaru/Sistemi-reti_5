import math
#from sympy import prime #scrivo prime(n)

def mcm(p, q):
    return (p*q)/(math.gcd(p, q))

def main():
    """
    Author: Noemi Baruffolo
    date: 06/11/2024
    es. rsa codifica una frase e viceversa (uso ord() per codice Ascii)

    prendo ogni lettera, la converto in asci con ord(), la inserisco nella lista numeri, faccio il calcolo scorrendo ogni elemento
    della lista con la formula del n.7 e verifico con il n.8
    """
    #1
    p = 47
    q = 691
    n = p * q #2
    m = int(mcm(p-1, q-1)) #3

    #4
    for i in range (2, m+1):
        if math.gcd(i, m) == 1:
            c = i
            break
            #print(f"c: {c}")
        '''else:
            print("Errore ciclo1!")'''

    #5
    for i in range (3, m+1):
        if ((c*i)%m) == 1:
            d = i
            break
            #print(f"d: {d}")
        '''else:
            print("Errore ciclo2!")'''
        
    #6
    print(f"La chiave pubblica è composta da: {n}(n) e {c}(c)")
    print(f"La chiave privata è composta da: {p}(p), {q}(q), {m}(m) e {d}(d)")

    #7
    frase = input("Inserisci una frase: ")
    carattere = []
    numeri = []
    b = []

    for char in frase:
        carattere.append(char)
    
    for i in range(len(carattere)):
        numeri[i] = ord(carattere[i])

    for pos in range(len(numeri)):
        b[pos] = ((numeri[pos] ** c)%n)
        print(f"b: {b[pos]}")

    #8
    for posiz in range(len(b)):
        if ((b[posiz] ** d)%n) == numeri:
            print(f"{b[posiz]}(b) e {numeri[posiz]}(a) -- Corretto!")
        else:
            print(f"{b[posiz]}(b) e {numeri[posiz]}(a) -- Sbagliato!")

if __name__ == "__main__":
     main()