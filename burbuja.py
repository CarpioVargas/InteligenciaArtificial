from time import time

lista = [2, 19, 10, 1, 40]

#inicia tiempo de ejecucion
tiempo_inicial = time()

def ordenamientoBurbuja(lista):
	""" Ordenar una lista utilizando el metodo de Burbuja """

	for i in range (1, len(lista)):
		# Scanea la lista, quitando los valores ya ordenados
		for j in range (len(lista) - i):
			# La posicion actual es mayor a la siguiente?
			if (lista[j] > lista[j+1]):
				# Intercambia los valores de la posicion actual con la siguiente 
				lista[j+1], lista[j] = lista[j], lista[j+1]
	print lista

ordenamientoBurbuja(lista)
#Fin del tiempo de ejecucion
tiempo_final = time()
print tiempo_final - tiempo_inicial








