from time import time

lista = [2, 19, 10, 1, 40]
tiempo_inicial = time()

def ordenamientoBurbuja(lista):
	for i in range (1, len(lista)):
		for j in range (len(lista) - i):
			if(lista[j] > lista[j+1]):
				lista[j+1], lista[j] = lista[j], lista[j+1]
	print lista

ordenamientoBurbuja(lista)
tiempo_final = time()
print tiempo_final - tiempo_inicial








