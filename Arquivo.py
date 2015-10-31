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

	def abrir_arquivo(self, arquivo, modo_leitura):
		return open(arquivo, modo_leitura)

	def ler_arquivo(self):
		arq = self.abrir_arquivo(self.arquivo_entrada, "r")
		lista_dados = arq.readlines()
		arq.close()
		return lista_dados

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

	def pega_vertices(self, vertices):
		for i in vertices[:1]:
			
			aux = i.split(' ')
			
			for j in aux[:-1]:
				self.vertices.append(j)

			ultimo_elemento = aux[len(aux) - 1]
			self.vertices.append( ultimo_elemento[:-2] )

	def ler_entrada(self):
		dados = self.ler_arquivo()
		dados_distribuidos = self.distribui_dados(dados)
		self.pega_vertices(dados_distribuidos['grafo'])
		#print(self.vertices)

	def grava_saida(self):
		pass	
