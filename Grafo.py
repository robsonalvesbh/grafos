import sys

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

	def busca_em_largura(self, origem, destino):

		v_atual = origem
		fila = []
		visitados = []
		respostas = [[v_atual]]

		while v_atual != destino:

			try:
				if not v_atual in visitados:
					for i in self.lista_adjacencia[v_atual]:
						if i[0] not in visitados:
							visitados += [v_atual]
							fila.append(i[0])
				
				respostas.append(list(fila))

				if fila:
					v_atual = fila.pop(0)
				else:
					break
			except:
				return respostas

		return respostas

	def busca_em_profundidade(self, origem, destino):

		v_atual = origem
		pilha = []
		visitados = []
		respostas = [v_atual]

		while v_atual != destino:

			#se o vertice atual ainda nao foi visitado
			if not v_atual in visitados:
				visitados.append(v_atual) #adiciona a lista de visitados
				pilha.append(v_atual) #adiciona a pilha

			existe_vizinho = [False] #lista auxiliar que vai verificar se existe visito para meu vertice atualz

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
				visitados.append(v_atual) #falo que esse vertice que nao possui vizinhos ja foi vizitado
				respostas.pop(-1) #removo ele da pilha de resposta
				continue #continue informa para meu loop parar aqui e começar na proxima volta

			#verifico se existe vizinho (filhos do vertice atual) a serem percorridos
			if existe_vizinho[0]:
				respostas.append(existe_vizinho[1]) #coloca o elemento na nossa pilha de resposta
				v_atual = existe_vizinho[1] #o vertice atual agora é o vizinho
			else: #se nao existe um vizinho
				pilha.pop(-1) #removo o elemento do topo da pilha
				v_atual = pilha[len(pilha) - 1] #vertice passa a ser o ultimo elemento da pilha 
				respostas.pop(-1) #removo da pilha de resposta
				#se a pilha estiver vazia, paro o loop com break
				if pilha:
					break
			

		return respostas


