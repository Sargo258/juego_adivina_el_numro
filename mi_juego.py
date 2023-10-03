
import random

name = input('Dime tu nombre: ')
print(f'Bueno, {name} he pensado un número entre 1 y 100, y tienes solo ocho intentos para adivinar cuál crees que es el número ')

secret_number = random.randint(1, 100)
attempts = 0

while attempts < 8:
    try:
        guess = int(input('Introduce tu suposición: '))
    except ValueError:
        print('Por favor, ingresa un número válido.')
        continue

    attempts += 1

    if guess < secret_number:
        print('El número es mayor. Intenta de nuevo.')
    elif guess > secret_number:
        print('El número es menor. Intenta de nuevo.')
    else:
        print(f'¡Felicidades, {name}! Has adivinado el número en {attempts} intentos.')
        break
else:
    print(f'Lo siento, {name}. Has agotado tus 8 intentos. El número secreto era {secret_number}.')
