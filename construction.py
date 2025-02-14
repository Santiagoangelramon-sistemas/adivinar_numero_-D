import random

maq = random.randint(1, 100)
i = 1
print("-----------------------------------------------")
print("¡Bienvenido al juego de adivinar el numero!")
print("Estoy pensando en un numero entre 1 y 100.")
print("-----------------------------------------------")
while True:

    n = int(input("Introduce un numero:  "))


    if n != maq:
        if n < maq:
            print("El valor es mayor al elegido.")
        else:
            print("El valor es menor al elegido.")
        i += 1
    else:
        print(f"¡Felicidades! Adivinastes el numero en {i} intentos.")
        break