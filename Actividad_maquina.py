bebidas = [
    ["Coca Cola", 15, 1.50],
    ["Fanta naranja", 10, 1.40],
    ["Agua", 20, 1.00],
    ["Nestea", 2, 1.60],
    ["Aquarius", 12, 1.70]
]

menu = []
ventas = []
precio_total = 0

monedas = [0.05, 0.10, 0.20, 0.50, 1, 2]

while menu != 5:
    menu = int(input("Elige la opcion que quieras:\n"
    "0.Coca cola\n"
    "1.Fanta naranja\n"
    "2.Agua\n"
    "3.Nestea\n"
    "4.Aquarius\n"
    "5.OFF \n"
    ":"))

    if menu == 0:
        nombre_producto = bebidas[0][0]
        stock_producto = bebidas[0][1]
        precio_producto = bebidas[0][2]
        pago = 0
        if stock_producto>0:
            bebidas[0][1] -= 1
            ventas.append(nombre_producto)
            ventas.append(precio_producto)
            precio_total += precio_producto
            print("Has comprado CocaCola precio: ",precio_producto)

            while precio_producto < pago:
                pago2 = input("Introduzca moneda: ")
                pago += pago2

        elif stock_producto == 0:
            print("Este tipo de bebida esta agotada")

    if menu == 1:
        nombre_producto = bebidas[1][0]
        stock_producto = bebidas[1][1]
        precio_producto = bebidas[1][2]
        if stock_producto>0:
            bebidas[1][1] -= 1
            ventas.append(nombre_producto)
            ventas.append(precio_producto)
            precio_total += precio_producto
            print("Has añadido", ventas)
        elif stock_producto == 0:       
            print("Este tipo de bebida esta agotada")
    
    if menu == 2:
        nombre_producto = bebidas[2][0]
        stock_producto = bebidas[2][1]
        precio_producto = bebidas[2][2]
        if stock_producto>0:
            bebidas[2][1] -= 1
            ventas.append(nombre_producto)
            ventas.append(precio_producto)
            precio_total += precio_producto
            print("Has añadido", ventas)
        elif stock_producto == 0:       
            print("Este tipo de bebida esta agotada")

    if menu == 3:
        nombre_producto = bebidas[3][0]
        stock_producto = bebidas[3][1]
        precio_producto = bebidas[3][2]
        if stock_producto>0:
            bebidas[3][1] -= 1
            ventas.append(nombre_producto)
            ventas.append(precio_producto)
            precio_total += precio_producto
            print("Has añadido", ventas)
        elif stock_producto == 0:        
            print("Este tipo de bebida esta agotada")

    if menu == 4:
        nombre_producto = bebidas[4][0]
        stock_producto = bebidas[4][1]
        precio_producto = bebidas[4][2]
        if stock_producto>0:
            bebidas[4][1] -= 1
            ventas.append(nombre_producto)
            ventas.append(precio_producto)
            precio_total += precio_producto
            print("Has añadido", ventas)
        elif stock_producto == 0:        
            print("Este tipo de bebida esta agotada")

if menu == 5:
    print("Las ventas del día son las siguientes: ", ventas)
    print("Recaudación total es de: ", precio_total)