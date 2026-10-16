puntuacion = 0
import random
intentos = 0

while puntuacion <50:
    numero = random.randint(1, 6)
    print (numero)
    if numero <6:
        puntuacion += numero
        intentos +=1
    else:
        puntuacion += 12
        intentos +=1
    if puntuacion>50:
        

print("Tu puntuación es de ",puntuacion)
print("Tu numero de intentos es de ", intentos)
