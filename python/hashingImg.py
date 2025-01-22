import hashlib

def hash_image(file_path):
    # Apre il file immagine in modalità binaria
    with open(file_path, 'rb') as image_file:
        # Legge il contenuto del file
        file_data = image_file.read()

        # Calcola l'hash SHA-256
        sha256_hash = hashlib.sha256(file_data).hexdigest()

        return sha256_hash

def main():
    """
    author: Noemi Baruffolo
    date: 06/12/2024
    Descrizione: data una stringa, calcolare il suo hash utilizzando hashing
    """
    file_path = input("Inserisci il percorso dell'immagine da hashare: ")

    hash_value = hash_image(file_path)
    print(f"L'hash SHA-256 dell'immagine è: {hash_value}")

if __name__ == "__main__":
    main()
