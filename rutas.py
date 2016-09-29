# [1] = [2, 3, 6, 8]
# [2] = [1, 3, 4, 5, 8]
# [3] = [1, 2, 4]
# [4] = [2, 3, 5, 8]
# [5] = [2, 4, 6]
# [6] = [1, 7]
# [7] = [6, 8]
# [8] = [1, 2, 4, 7]

mat = {'1': ['2', '3', '6', '8'],
         '2': ['1', '3','4','5','8'],
         '3': ['1','2','4'],
         '4': ['2','3','5','8'],
         '5': ['2','4','6'],
         '6': ['1','7'],
         '7': ['6','8'],
         '8': ['1','2', '4', '7']
         }

def findthis(mat, start, end, route=[]):
	route = route + [start]

	if start == end:
		return route

	for i in mat[start]:
		if i not in route:
			newroute = findthis(mat, i, end, route)
			return newroute
	return None

start = raw_input("Dame el inicio: ")
end = raw_input("Dame el destino: ")
print findthis(mat, start, end)