matx = { '1': ['2', '3', '6', '8'],
         '2': ['1', '3','4','5','8'],
         '3': ['1','2','4'],
         '4': ['2','3','5','8'],
         '5': ['2','4'],
         '6': ['1','7'],
         '7': ['6','8'],
         '8': ['1','2', '4', '7']
         }

def find_route (matx, start, end, visited = []):
	visited = visited + [start]
	if start == end:
		print visited

	if matx.has_key(start) and matx.has_key(end):
		
		for currentNode in matx[start]:
			if not currentNode in visited:
				find_route(matx, currentNode, end, visited)
	else:
		print "Does not exist"

start, end = raw_input("start: "), raw_input("end: ")
find_route(matx, start, end)
