import socket
import threading, random
import numpy as np
from sympy import prime

#alice

MY_ADDRESS = ("127.0.0.1", 43211)
BUFFER_SIZE = 4096


def main():
    """
    Author: Noemi Baruffolo
    date: 07/11/2024
    es. preparazione verifica (server tcp)
    text: vedi "Esercitazione - preparazione alla verifica" su Classroom
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(MY_ADDRESS)
    s.listen()

    
    n = prime(np.random.choice(np.arange(500, 600)))
    
    g = random.randint(2, n-1)
    a = random.randint(2, n-1) # privato
    print(n, g)
    A = (g**a) % n
    print(f"A = {A}")
    connection, _ = s.accept()

    connection.sendall(f"{g}|{n}|{A}".encode())

    mess = connection.recv(BUFFER_SIZE).decode()

    B = int(mess)
    print(f"B = {B}")
    print((B**a) % n) #chiave di sessione

    connection.close()

    s.close()




    

if __name__ == "__main__":
    main()