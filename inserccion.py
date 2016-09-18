from time import time

lista = [2, 8, 6, 1, 9, 0, -4]

#inicia el tiempo de ejecucion
tiempo_inicial = time()

def ordenamientoInserccion(lista):
	""" Ordenar una lista utilizando el metodo de Inserccion """
    
    for i in range(len(lista)):
    	#Encontrar la posicion con el numero mas chico
    	#Empezar desde la posicion actual
        pos_min = i

        for j in range(i + 1, len(lista)):

        	#Es esta posicion mas chica?
            if lista[j] < lista[pos_min]:

            	#Si lo es marcar como la mas chica
                pos_min = j

            #Intercambiar los dos valores    
        	lista[pos_min], lista[i] = lista[i], lista[pos_min]
        
    print lista

ordenamientoInserccion(lista)
#termina el tiempo de ejecucion
tiempo_final = time()
print tiempo_final - tiempo_inicial
