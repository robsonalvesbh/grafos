class Arquivo(object):

	"""Método construtor da classe"""
	def __init__(self, arquivo_entrada, arquivo_saida):
		self.arquivo_entrada = arquivo_entrada
		self.arquivo_saida = arquivo_saida
		self.vertices = []
		self.arestas = []
		self.comandos = {}
		self.grafo = {}

	def get_file_name(self):
		print("O nome do arquivo de entrada e %s " % self.arquivo_entrada)
		print("E o arquivo de saida e %s" % self.arquivo_saida)

	#Função abrir aquivo recebe 2 parametros (arquivo e o modo de abertura) e retorna o arquivo aberto
	def abrir_arquivo(self, arquivo, modo_abertura):
		return open(arquivo, modo_abertura)

	#Função ler os dados do arquivo de entrada grava em uma lista de dados e retorna está lista de dados
	def ler_arquivo(self):
		arq = self.abrir_arquivo(self.arquivo_entrada, "r")
		lista_dados = arq.readlines()
		arq.close()
		return lista_dados

	#função que separa a lista de dados em 3 partes, vertices, arestas e comandos
	def distribui_dados(self, lista):
		indice_vertice = lista.index("ARESTAS\n")
		indice_aresta = lista.index("COMANDOS\n")

		dados = {}
		dados['grafo'] = []
		dados['arestas'] = []
		dados['comandos'] = []

		for i in lista[1:indice_vertice - 1]:
			dados['grafo'].append(i)

		for i in lista[indice_vertice + 1:indice_aresta - 1]:
			dados['arestas'].append(i)

		for i in lista[indice_aresta + 1: -1]:
			dados['comandos'].append(i)	

		return dados

	#função que pega os vertices
	def pega_vertices(self, vertices):
		#percorre a lista de vertices 
		for i in vertices[:1]:
			#separa todos os elemento em uma lista, separando pelo espaço
			aux = i.split(' ')
			#percorre a lista que foi criada anteriormente menos o ultimo elemento
			for j in aux[:-1]:
				#adiciona cada elemento na lista self.vertices
				self.vertices.append(j)
			#joga o ultimo elemento para dentro da variavel ultimo_elemento
			ultimo_elemento = aux[len(aux) - 1]
			#joga para dentro da lista self.vertices eliminando os 2 ultimos caracteres da lista que são ';\n'
			self.vertices.append( ultimo_elemento[:-2] )

	#função que pega as arestas
	def pega_arestas(self, arestas):
		#percorre a lista de arestas 
		for i in arestas:
			#separa todos os elemento em uma lista, separando pelo espaço
			aux = i.split(' ')	
			#cria uma lista auxiliar vazia
			lista_aux = []
			#percorre a lista que foi criada anteriormente menos o ultimo elemento
			for j in aux[:-1]:
				#adiciona cada elemento na lista_aux
				lista_aux.append(j)
			#pega o ultimo elemento
			ultimo_elemento = aux[len(aux) - 1]
			
			#verifica se o ultimo elemento (peso da aresta) é igual ',\n' ou igual ';\n'
			if ultimo_elemento == ',\n' or ultimo_elemento == ';\n':
				#se a aresta não tiver peso adiciono peso 1
				lista_aux.append( '1' )
			else:
				#se tiver adiciono o peso
				lista_aux.append( ultimo_elemento[:-2] )
			#em cada loop do for adiciono a lista contendo (vertice_origem, vertice_destino, peso) na lista self.arestas
			self.arestas.append(lista_aux)

	#função que ler o arquivo de entrada
	def ler_entrada(self):
		dados = self.ler_arquivo()
		dados_distribuidos = self.distribui_dados(dados)
		self.pega_vertices(dados_distribuidos['grafo'])
		self.pega_arestas(dados_distribuidos['arestas'])
		#print(self.vertices)

	#função que grava a resposta no arquivo de saida
	def grava_saida(self):
		pass	
