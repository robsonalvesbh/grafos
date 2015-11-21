import sys
import math

class Grafo(object):

	"""Construtor da classe Grafo"""
	def __init__(self, dados):
		self.dados = dados
		self.lista_adjacencia = {}

	def cria_lista_adjacencia(self):

		try:
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
						# verifico se o vertice destino está na lista de adjacencia, se nao tiver crio um lista para ela
						if not i[1] in self.lista_adjacencia:
							self.lista_adjacencia[i[1]] = [] #cria a lista vazia
						#se nao existi o elemento origem na lista destino, adiciono ele
						if not i[0] in self.lista_adjacencia[i[1]]: 
							self.lista_adjacencia[i[1]].append([i[0], 1])
				else:
					if not i[0] in self.lista_adjacencia:
						self.lista_adjacencia[i[0]] = []

					self.lista_adjacencia[i[0]].append([i[1], int( i[2] )])

					if self.dados['eh_digrafo'] == False:
						if not i[1] in self.lista_adjacencia:
							self.lista_adjacencia[i[1]] = []
						if not i[0] in self.lista_adjacencia[i[1]]:
							self.lista_adjacencia[i[1]].append([i[0],int( i[2] )])

			return True
		except:
			return False


	def calcula_distancia(self, caminho):
		
		caminho_entrada = caminho
		v_atual = caminho.pop(0)
		distancia = 0

		try:
			while caminho:

				for aresta in self.lista_adjacencia[v_atual]:

					if caminho[0] == aresta[0]:
						distancia += aresta[1]
						v_atual = caminho.pop(0)
						break;

			return distancia
		except:
			return None

	"""
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
	"""

	def busca_em_largura(self, origem, destino):

		v_atual = origem
		fila = []
		visitados = []
		respostas = [[v_atual]]

		try:
			while v_atual != destino:

				if v_atual in self.lista_adjacencia:
					if not v_atual in visitados:
						for i in self.lista_adjacencia[v_atual]:
							if i[0] not in visitados:
								visitados += [v_atual]
								fila.append(i[0])
				else:
					visitados += [v_atual]

				if fila:
					respostas.append(list(fila))
					v_atual = fila.pop(0)
				else:
					break

			return respostas
		except:
			return None

	""" profundidade usando pilha
	def __busca_em_profundidade(self, origem, destino):

		v_atual = origem
		pilha = []
		visitados = []
		respostas = [v_atual]

		while v_atual != destino:

			#se o vertice atual ainda nao foi visitado
			if not v_atual in visitados:
				visitados.append(v_atual) #adiciona a lista de visitados
				pilha.append(v_atual) #adiciona a pilha

			existe_vizinho = [False] #lista auxiliar que vai verificar se existe visito para meu vertice atual

			#verifica se meu vertice atual possui vizinhos
			if v_atual in self.lista_adjacencia:
				#percorro a lista de vizinhos
				for i in self.lista_adjacencia[v_atual]:
					#se meu vizinho ainda nao foi visitado
					if not i[0] in visitados:
						existe_vizinho[0] = True #primeira posicao vai afirmar que existe vizinho que ainda nao foi visitado
						existe_vizinho.append(i[0]) #segunda posicao guarda o valor do vizinho
						break
			else: #se nao possui vizinhos
				pilha.pop(-1) #volto para o vertice anterior
				v_atual = pilha[len(pilha) - 1] # meu vertice atual recebe o vertice anterior
				respostas.append(v_atual)
				visitados.append(v_atual) #falo que esse vertice que nao possui vizinhos ja foi vizitado
				#respostas.pop(-1) #removo ele da pilha de resposta
				continue #continue informa para meu loop parar aqui e começar na proxima volta

			#verifico se existe vizinho (filhos do vertice atual) a serem percorridos
			if existe_vizinho[0]:
				v_atual = existe_vizinho[1] #o vertice atual agora é o vizinho
				respostas.append(v_atual) #coloca o elemento na nossa pilha de resposta
			else: #se nao existe um vizinho
				pilha.pop(-1) #removo o elemento do topo da pilha
				v_atual = pilha[len(pilha) - 1] #vertice passa a ser o ultimo elemento da pilha 
				respostas.append(v_atual)
				#respostas.pop(-1) #removo da pilha de resposta
				#se a pilha estiver vazia, paro o loop com break
				if len(pilha) == 0:
					break
			

		return respostas 
	"""

	def busca_em_profundidade(self, origem, destino):

		fila = []
		visitados = []
		respostas = [[origem]]
		v_atual = origem

		try:
			while v_atual != destino:

				if v_atual in self.lista_adjacencia:
					
					if not v_atual in visitados:
						indice = 0
						for i in self.lista_adjacencia[v_atual]:
							if i[0] not in visitados:
								visitados += [v_atual]
								fila.insert(indice, i[0])
								indice += 1
				else:
					visitados += [v_atual]

				if len(fila) > 0:
					respostas.append(list(fila))
					v_atual = fila.pop(0)
				else:
					break
			
			return respostas
		except:
			return None

	def dijkstra(self, origem, destino):

		v_atual = []
		distancia = {}
		visitados = []
		v_anterior = {}
		prioridade = []

		#Cria peso infinito para todas as arestas
		for i in self.lista_adjacencia:
			for j in self.lista_adjacencia[i]:
				distancia[j[0]] = math.inf

		distancia[origem] = 0

		prioridade.append([origem, distancia[origem]])

		try:
			while len(prioridade) > 0:

				v_atual = list(prioridade.pop(0))

				if v_atual[0] in self.lista_adjacencia:

					if not v_atual[0] in visitados:

						visitados.append(v_atual)

						for i in self.lista_adjacencia[v_atual[0]]:

							if distancia[i[0]] > (distancia[v_atual[0]] + i[1]):
								
								distancia[i[0]] = distancia[v_atual[0]] + i[1]
								prioridade.append( [ i[0], distancia[i[0]] ] )
								v_anterior[i[0]] = v_atual[0]

				else:
					continue

			caminho = [destino]
			v_aux = destino

			while(True):

				if v_aux in v_anterior:
					caminho.append( v_anterior[v_aux] )
					v_aux = v_anterior[v_aux]
				else:
					break

			return {'caminho': caminho, 'distancia': distancia[destino]}
		except:
			return None

	def prim(self, origem):

		try:

			visitados = [str(origem)]
			vertices = list(self.dados['vertices'])
			vertices.remove(str(origem))
			distancia = 0
			respostas = {'caminho': [], 'distancia': None}

			while len(vertices) > 0:

				a_menor = math.inf
				v_menor = None
				v_atual = None

				for v in visitados:
					if v in self.lista_adjacencia:
						for i in self.lista_adjacencia[v]:

							if not i[0] in visitados:

								if i[1] < a_menor:
									a_menor = i[1]
									v_menor = i[0]
									v_atual = v
									distancia += i[1]

				respostas['caminho'].append( list([v_atual, v_menor, a_menor]) )

				visitados.append(v_menor)
				vertices.remove(v_menor)
			
			respostas['distancia'] = distancia

			return respostas
		except:
			return None

	def detecta_ciclo(self, vertices):

		caminho = list(vertices)
		visitados = []
		v_atual = None

		while len(caminho) > 0:
			v_atual = caminho.pop(0)

			if not v_atual in visitados:
				visitados.append(v_atual)
			else:
				return True

		return False

	def kruskal(self):

		#Cria peso infinito para todas as arestas
		for i in self.lista_adjacencia:
			for j in self.lista_adjacencia[i]:
				print(j)