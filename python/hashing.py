import hashlib

def main():
    """
    author: Noemi Baruffolo
    date: 06/12/2024
    Descrizione: data una stringa, calcolare il suo hash utilizzando hashing
    """
    # Chiedi all'utente una stringa in input
    user_input = input("Inserisci una stringa da hashare: ")
    
    # Calcola l'hash usando SHA-256
    m = hashlib.sha256()
    m.update(user_input.encode('utf-8'))  # Codifica la stringa in byte
    hash_value = m.hexdigest()  # Ottieni l'hash esadecimale

    print(f"L'hash SHA-256 della stringa inserita è: {hash_value}")

if __name__ == "__main__":
    main()
