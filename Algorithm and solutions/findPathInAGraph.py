
graph = {'A': ['B', 'C'],
		'B': ['C', 'D'],
		'C': ['D'],
		'D': ['C'],
		'E': ['F'],
		'F': ['C']}

def find_path(graph, start, end, path=[]): # notice the default value for the function Love python for that
	path = path + [start] # start from the node
	if(start == end):
		return path
	if not graph.has_key(start):
		return None #invalid graph

	for node in graph[start]:
		if node not in path:
			newpath = find_path(graph,node,end,path)
			if newpath: return newpath
	return None

def main():
	print(find_path(graph,'A', 'D'))


if __name__ == '__main__':
	main()