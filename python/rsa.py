import math
#from sympy import prime #scrivo prime(n)

def mcm(p, q):
    return (p*q)/(math.gcd(p, q))

def main():
    """
    Author: Noemi Baruffolo
    date: 06/11/2024
    es. rsa (codifica un numero)
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
    a = int(input(f"Inserisci un numero compreso tra 0 e {n}: "))
    b = ((a ** c)%n)
    print(f"b: {b}")

    #8
    if ((b ** d)%n) == a:
        print(f"{b}(b) e {a}(a) -- Corretto!")
    else:
        print(f"{b}(b) e {a}(a) -- Sbagliato!")

if __name__ == "__main__":
     main()