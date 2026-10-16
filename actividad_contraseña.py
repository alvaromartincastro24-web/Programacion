contraseña = []

contraseña = input("Introduce tu contraseña: ")

intento = []

for i in range(1,5):
    intento = input("Pon la contraseña: ")
    if intento != contraseña:
        print("No es la contraseña llevas intentos ",i)
    else:
        print("Contraseña correcta")
        break

else:
    print("Te has quedado sin intentos")
    
