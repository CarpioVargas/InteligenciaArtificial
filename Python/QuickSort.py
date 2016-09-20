from time import time
lst = [2, 5, 1]

initial_time = time()
def quickSort(lst, start, end):
	if start >= end: return

	# i, j es igual al valor de inicio y final de la lista
	i, j = start, end
	# Se obtiene el pivote del valor medio de la lista
	pivot = lst[(start + end) / 2]
	while i <= j:
		
		# Recorre la mitad izquierda de la lista hasta encontrar un valor mayor al pivote
		while lst[i] < pivot:
			i += 1

		# Recorre la mitad derecha de la lista hasta encontrar un valor menor al pivote 	
		while lst[j] > pivot:
			j -= 1
		
		if i <= j:
			# Cambia los valores en la lista
			lst[i], lst[j] = lst[j], lst[i]
			i, j = i + 1, j - 1

	quickSort(lst, start, j)
	quickSort(lst, i, end)
	return lst

l = quickSort(lst, 0, len(lst) - 1); print l
final_time = time()
print final_time - initial_time


# first_while  ->  2 < 5 
# 				   i = 1
# first_while  ->  5 < 5 
#				   i = 1
# second_while ->  1 > 5
#				   j = 2
# if_sentence  ->  1 <= 2
# 
# lst = [2, 5, 1]
# i = 1, j = 2
# lst = [2, 1, 5]
# i = 2, j = 1
# quickSort(lst, 0, 1)
# quickSort(lst, 2, 2)
# i = 0, j = 1
# first_while  -> 2 < 1
# 				  i = 0
# second_while -> 2 > 1
# 				  j = 1
# if_sentence  -> 0 <= 1
# lst = [2, 1, 5]
# i = 0, j = 1
# lst = [1, 2, 5]
# i = 1, j = 0
 





