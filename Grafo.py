class Grafo(object):

	"""Construtor da classe Grafo"""
	def __init__(self, dados):
		self.dados = dados
		self.lista_adjacencia = {}

	def cria_lista_adjacencia(self):
		#percorro a lista de arestas
		for i in self.dados['arestas']:
			#verifico se elas não possui peso
			if self.dados['tem_peso'] == False:
				#verifica se o vertice de origem está presente na lista de adjacencia
				if not i[0] in self.lista_adjacencia:
					#se nao tiver crio uma lista vazia para este vetor
					self.lista_adjacencia[i[0]] = []
				#adiciono na lista do vertice de origem, o vertice de destino e o peso 1
				self.lista_adjacencia[i[0]].append([i[1], 1])
				#verifico se o grafo é direcionado ou um digrafo
				if self.dados['eh_digrafo'] == False:
					if not i[1] in self.lista_adjacencia:
						self.lista_adjacencia[i[1]] = []
					if not i[0] in self.lista_adjacencia[i[1]]:
						self.lista_adjacencia[i[1]].append([i[0], 1])
			else:
				if not i[0] in self.lista_adjacencia:
					self.lista_adjacencia[i[0]] = []
				self.lista_adjacencia[i[0]].append([i[1], i[2]])

				if self.dados['eh_digrafo'] == False:
					if not i[1] in self.lista_adjacencia:
						self.lista_adjacencia[i[1]] = []
					if not i[0] in self.lista_adjacencia[i[1]]:
						self.lista_adjacencia[i[1]].append([i[0], i[2]])

	def calcula_distancia(self, caminho):

		caminho_entrada = caminho
		v_atual = caminho.pop(0)
		distancia = 0

		while caminho:

			for aresta in self.lista_adjacencia[v_atual]:

				if caminho[0] == aresta[0]:
					distancia += aresta[1]
					v_atual = caminho.pop(0)
					break;

		return distancia

	def encontra_caminho(self, origem, destino):
		
		caminho = []
		v_atual = origem
		caminho += [origem]
		distancia = 0

		while v_atual != destino:
			
			lista_aux = []

			if v_atual == destino:
				return {"caminho": caminho, "distancia": distancia}

			if not v_atual in self.lista_adjacencia:
				return None

			for aresta in self.lista_adjacencia[v_atual]:
				lista_aux.append(aresta[0])

			for aresta in self.lista_adjacencia[v_atual]:
				
				if destino in lista_aux:
					indice = lista_aux.index(destino)
					distancia += self.lista_adjacencia[v_atual][indice][1]
					v_atual = self.lista_adjacencia[v_atual][indice][0]
					caminho += [v_atual]	
					break

				if aresta[0] not in caminho:
					
					v_atual = aresta[0]
					distancia += aresta[1]
					caminho += [v_atual]
					break

		return {"caminho": caminho, "distancia": distancia}