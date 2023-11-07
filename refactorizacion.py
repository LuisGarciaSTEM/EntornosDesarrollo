"""
Bateria de pruebas simplificadas:
Crear una funcion que se va a llamar probandoCalcularDoble() que va a tener
una lista de números "aleatorios/convenientes" [introducidos por nosotros
manualmente] que vamos a recorrer con un bucle for. Por cada número de la lista
va a llamar a la funcion calcularDoble(numero), y a imprimir por pantalla:
"El doble de {numero} es {dobleNumero}"
"""


def calcularDoble(numero):
    return numero * 2


def probandoCalcularDoble():
    numerosProbar = [2, 5, 7, 10, 15]
    for numero in numerosProbar:
        dobleNumero = calcularDoble(numero)
        print("El doble de " + str(numero) + " es " + str(dobleNumero))


print (probandoCalcularDoble())
