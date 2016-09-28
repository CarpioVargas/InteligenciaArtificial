# [1] = [2, 3, 6, 8]
# [2] = [1, 3, 4, 5, 8]
# [3] = [1, 2, 4]
# [4] = [2, 3, 5, 8]
# [5] = [2, 4]
# [6] = [1, 7]
# [7] = [6, 8]
# [8] = [1, 2, 4, 7]

lst	 = [	
			[2,3,6,8,0], 
			[1,3,4,5,8],
			[1,2,4,0,0],
			[2,3,5,8,0],
			[2,4,0,0,0],
			[1,7,0,0,0],
			[6,8,0,0,0],
			[1,2,4,7,0]
		]

def findthis(lst, start, end, current):
	start -= 1
	if start == end:
		return

	currentArray = lst[start]
	for i in range (len(currentArray)):
		if lst[start][i] == end:
			print start +1, lst[start]
			return
	
	if current < len(currentArray):
		start = currentArray[current]
		current += 1
		findthis(lst, start, end, current)
	else:
		findthis(lst, currentArray[0], end, current)
	


findthis(lst, 1, 5, 0)
	

