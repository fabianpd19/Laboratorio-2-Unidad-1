
#encabezado del programa a realizar (presentación)
#introducción al programa
def encabezado ():
    print("Ejercicio - Laboratorio 2 - Unidad 1.")
    print("Fabián Alexander Palma Dueñas.")
    print("Programación Orientada a Objetos [NRC 6181].")
    print("Problelma: Hallar la potencia de cualquier número x^y.")
#encabezado(nombre)
#funcion para resolver el programa asignado
def ejercicioPotencia(base,potencia):
    #realizamos el respectivo proceso para encontrar la potencia de un número
    resultadoPotencia=base**potencia
    #mostramos los datos ingresados tanto como el respectivo resultado
    print("El resultado es: ",base,"^",potencia, "=", resultadoPotencia)
    return resultadoPotencia
#llamado respectivo a cada una de las funciones para ejecutarlas
encabezado()
#pedir datos al usuario para resolver el problema
#una vez usamos los argumentos, los cuales serán x=base y la y=potencia
x=int(input("\nIngrese el número que desea elevar a una potencia: "))
y=int(input("Ingrese la potencia:  "))
ejercicioPotencia(x,y)
