from ast import Constant


edad = int(input("Por favor, ingrese su edad: "))

edad_jubilatoria = 64

if edad > edad_jubilatoria:
    print("Ya está en edad de jubilarse!")
else:
    print("Aún está en edad de trabajar!")
