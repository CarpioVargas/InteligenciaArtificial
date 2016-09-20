from time import time
lst = [2, 5, 8, 1, 3]

# tiempo inicial de la ejecucion
tiempo_inicial = time()

def shellSort(lista):
    mid = len(lista) // 2
    while mid > 0:
        #recorre a partir de la mitad 
        for i in range(mid, len(lista)):
            val = lista[i]
            j = i
            # Mientras encuentre un numero mas chico en la particion lo cambia por el actual 
            while j >= mid and lista[j - mid] > val:
                lista[j] = lista[j - mid]
                j -= mid
            lista[j] = val      
        mid //= 2
    print lista
        
shellSort(lst)
# tiempo final de la ejecucion
tiempo_final = time()
print tiempo_final - tiempo_inicial



# gap = 2
# while 2 > 0:
#   desde i = 2 hasta 5
#       val = 8
#       j = 2
#       while 2 >= 2 and array[0] > 8
#           #
#       array[2] = 8
#       gap  = 1
#    desde i = 3 hasta 5
#       val = 1
#       j = 3
#       while 3 >= 1 and array[3-1=2] > 1
#           array[3] = array[3-1=2]
#           array[3] = 8
#           j = 3 - 1 
#           j = 2
#           lst = [2, 5, 1, 8, 3]
#       while 2 >= 1 and 5 > 1
#           array[2] = array[1]
#           array[2] = 5
#           j = 2 - 1
#           j = 1
#           lst = [2, 1, 5, 8, 3]
#       while 1 >= 1 and 2 > 1
#           array[1] = 2
#           j = 0
#       lst = [1, 2, 5, 8, 3]
#       gap = 1
#     desde i = 4 hasta 5
#        val = 3
#        j = 4
#        while 4 >= 1 and array[3] (8) > 3
#           array[4] = array[3]
#           j = 3
#        while 3>= 1 and array[2] (5) > 3
#           array[3] (5) = array[2]
#           j = 2
#           lst = [1, 2, 5, 5, 8]
#        array[2] = 3
#          lst = [1, 2, 3, 5, 8]
#        