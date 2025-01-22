import socket
import random
import socket

#bob

SERVER_ADDRESS = ("127.0.0.1", 43211)
BUFFER_SIZE = 4096

def main():
    """
    Author: Noemi Baruffolo
    date: 20/11/2024
    Descrizione: algoritmo di 
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(SERVER_ADDRESS)

    mess = s.recv(BUFFER_SIZE).decode()
    split_mess = mess.split("|")
    
    A = int(split_mess[2])
    g = int(split_mess[0])
    n = int(split_mess[1])
    print(n, g)

    b = random.randint(2, n) # privato

    B = (g**b) % n
    print(f"B = {B}")
    print(f"A = {A}")
    s.sendall(str(B).encode())

    print((A**b) % n) #chiave di sessione


    s.close()

if __name__ == "__main__":
    main()