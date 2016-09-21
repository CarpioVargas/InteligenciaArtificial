from time import time
lst = [3, 8, 5, 4]
tiempo_inicial = time()

def mergeSort(alist):
    if len(alist)>1:
    	# Se parte la lista en divisiones iguales 
    	# [3,8]
    	# [5,4]
    	# [3]
    	# [8]
    	# [5]
    	# [4]
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        # Se llama recursivamente hasta que la lista sea de tamano 1
        mergeSort(lefthalf)
        mergeSort(righthalf)
       
        i, j, k = 0,0,0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
            	alist[k] = lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1
            
        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1

        print alist
    	
mergeSort(lst)
tiempo_final = time ()
print tiempo_final - tiempo_inicial

