#necessita di una chiave, si somma la chiave decifrata al messaggio decifrato per avere il messaggio segreto e sommare %21

#creare classe che può contenere sia un testo in chiaro che un testo codificato

class Testo():
    def __init__(self, text, codif):
            self.text = text.lower()
            self.codif = codif
            self.cifrato = codif
            
    def codifica(self, dizio):
          if self.codif == False:
            listaCodif = [c for c in self.text]
            cifra = []
            for indice, car in enumerate(self.text):
                    cifra.append((dizio[car] + dizio[listaCodif[indice]])%21)
                    print(f"gia codificato")
          else:
              print(cifra)
    
    def decodifica(self, dizio):
          if self.codif == False:
               listaCodif = [c for c in self.text]
               cifra = []
               for indice, car in enumerate(self.text):
                    cifra.append((dizio[car] - dizio[listaCodif[indice]])%21) 
                    print(cifra)
          else:
              print(cifra)
    
def main():
    """
    Author: Noemi Baruffolo
    date: 15/01/2024
    es. 54 codice Cifrario di Vernam(segreti)
    text: data una stringa in input tradurla in codice cifrario di Vernam. Fare una classe Testo le cui istanze possano contenere un
    testo sia in chiaro che codificato.
    a : 0
    b : 1
    c : 2
    d : 3
    e : 4
    ...
    """
    dizNum = {}
    diz = {"a": 0, "b":1, "c" : 2, "d":3, "e": 4, "f":5, "g":6,"h":7,"i":8, "l": 9, "m": 10,"n":11,"o":12, "p":13,"q":14,"r":15,"s":16,"t":17,"u":18,"v":19, "z":20}
    print(diz)
    for chiave in diz:
         dizNum[diz[chiave]]=chiave
    print(dizNum)
    testo = Testo("ciao", False)
    testo.codifica(1234)
    print(testo)

if __name__ == "__main__":
     main()