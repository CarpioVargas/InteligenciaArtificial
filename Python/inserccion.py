from time import time

lista = [2, 8, 5, 1, 9]
# Inicio de la ejecucion
tiempo_inicio = time()

def ordenamientoInserccion(lista):
	""" Ordenar una lista utilizando el metodo de seleccion"""

	# Empezar en el segundo elemento de la lista (posicion 1)
	for i in range(1, len(lista)):
		# obtener el valor del elemento a insertar
		temp = lista[i]
		j = i - 1
		while j >= 0 and lista[j] > temp:
			lista[j+1] = lista[j]
			j -= 1
		lista[j+1] = temp
	print lista 

ordenamientoInserccion(lista)
tiempo_final = time()
print "Tiempo de ejecucion: ", tiempo_final - tiempo_inicio