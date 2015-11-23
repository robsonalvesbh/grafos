class Kruskal(Grafo):
	
	def __init__(self, lista):
		self.lista_adjacencia = lista
		self.vizinho = {}
		self.peso = {}

	def make_set(vertice):
	    vizinho[vertice] = vertice
	    peso[vertice] = 0

	def find(vertice):
	    if vizinho[vertice] != vertice:
	        vizinho[vertice] = find(vizinho[vertice])
	    return vizinho[vertice]

	def union(vertice1, vertice2):
	    root1 = find(vertice1)
	    root2 = find(vertice2)
	    if root1 != root2:
	        if peso[root1] > peso[root2]:
	            vizinho[root2] = root1
	        else:
	            vizinho[root1] = root2
	            if peso[root1] == peso[root2]: peso[root2] += 1

	def kruskal(graph):
	    for vertice in graph['vertices']:
	        make_set(vertice)

	    minimum_spanning_tree = set()
	    edges = list(graph['edges'])
	    edges.sort()
	    for edge in edges:
	        weight, vertice1, vertice2 = edge
	        if find(vertice1) != find(vertice2):
	            union(vertice1, vertice2)
	            minimum_spanning_tree.add(edge)
	    return minimum_spanning_tree

# graph = {
#         'vertices': ['A', 'B', 'C', 'D', 'E', 'F'],
#         'edges': set([
#             (1, 'A', 'B'),
#             (5, 'A', 'C'),
#             (3, 'A', 'D'),
#             (4, 'B', 'C'),
#             (2, 'B', 'D'),
#             (1, 'C', 'D'),
#             ])
#         }
# minimum_spanning_tree = set([
#             (1, 'A', 'B'),
#             (2, 'B', 'D'),
#             (1, 'C', 'D'),
#             ])
# assert kruskal(graph) == minimum_spanning_tree
