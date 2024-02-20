# Taller 2
#________________________________________________________________________________
# Desarrollado por Maria Andrea Mendez y Juan José Gómez Arenas
# Analisis de Algoritmos
# Pontificia Universidad Javeriana
#________________________________________________________________________________

#IMPORTO RANDOM PARA QUE SE REALICE CON UN NUMERO DIFERENTE CADA VEZ
#Esto, para probar el algoritmo en distintos escenarios
import random

print("Bienvenido al Juego de Adivinanza de Números")
print("_____________________________________________________")
print("- Piensa en un número natural y deja que el otro jugador adivine.")
print("- En este caso, tendras el rol del pensador.")
print("- Debes indicar para cada número, si es mayor, menor o igual.")
print("_____________________________________________________")

print("¡Empecemos!")

#En este caso se va a crear una lista ordenada desde el 1 hasta n
def crear_lista_hasta(n):
  if isinstance(n, int) and n > 0:
      return list(range(1, n + 1))
  else:
      print("Por favor, ingresa un número entero positivo.")


#Aqui escojo el limite superior de la lista, en este caso es un numero entre 1 y 100
n = random.randint(1, 100)

listaAdivinar = crear_lista_hasta(n)

print("Escoge un numero entre 1 y "+str(n))

print("____________________________________")

#Este es el ALGORITMO DE DIVIDIR Y VENCER donde recibe lista, limite inferior y superior
def adivinarDividirYVencer(listaAdivinar, b, e):
  #Caso base, donde se solapan los limites
  if b > e:
    return listaAdivinar[b]
  else:
    #Encuentro el pivote y pregunto si su numero esta en la posicion del pivote X[q]
    q = (b + e) // 2
    #Aqui como tal pregunto al jugador
    print("¿Tu numero es mayor (>), menor (<) o igual(=) a " + str(listaAdivinar[q]) + "?")
    print("____________________________________")
    respuesta = input("Ingresa '>', '<' o '=': ")
    
    #Dependiendo de la respuesta se llama a la funcion de nuevo con limites actualizados
    #Se esta asumiendo que el jugador siempre ingresa una respuesta valida

    if respuesta == ">":
      return adivinarDividirYVencer(listaAdivinar, q + 1, e)
    elif respuesta == "<":
      return adivinarDividirYVencer(listaAdivinar, b, q - 1)
    elif respuesta == "=":
      return listaAdivinar[q]



print("Tu numero es: "+str(adivinarDividirYVencer(listaAdivinar, 0, n)))
print("¡Bien Jugado!")
