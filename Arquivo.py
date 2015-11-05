from Erros import *

class Arquivo(object):

	"""Método construtor da classe"""
	def __init__(self, arquivo_entrada, arquivo_saida):
		self.arquivo_entrada = arquivo_entrada
		self.arquivo_saida = arquivo_saida
		self.vertices = []
		self.arestas = []
		self.comandos = []
		self.grafo = {}
		self.eh_digrafo = False
		self.tem_peso = False

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

		for i in lista[indice_aresta + 1:]:
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

		
		#percorre o vetor self.vertices e transforma-os seus itens em inteiros
		for i in range(len(self.vertices)):
			self.vertices[i] = int(self.vertices[i])
		#vertice[1] retorna "true ;" o split(' ') transforma ele em uma lista ['true', ';']
		#fazendo vertices[1].split(' ')[0] eu pego a primeira posicao que é true
		#e como uma string é nada mais que uma lista
		#e acrescentando o [0] a frente vertices[1].split(' ')[0][0] pegamos sempre a primeira letra 
		#que sempre será f ou t (f = false, t = true)
		self.eh_digrafo = vertices[1].split(' ')[0][0]
		#mesmo exemplo do digrafo acima
		self.tem_peso = vertices[2].split(' ')[0][0]
		

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
			if ultimo_elemento == ',\n' or ultimo_elemento == ';\n' or self.tem_peso == False:
				#se a aresta não tiver peso adiciono peso 1
				lista_aux.append( '1' )
			else:
				#se tiver adiciono o peso
				lista_aux.append( ultimo_elemento[:-2] )

			#percorre o vetor lista_aux e transforma-os seus itens em inteiros
			for i in range(len(lista_aux)):
				lista_aux[i] = int(lista_aux[i])

			#em cada loop do for adiciono a lista contendo (vertice_origem, vertice_destino, peso) na lista self.arestas
			self.arestas.append(lista_aux)

	def pega_comandos(self, comandos):
		#percorro a lista de comendos
		for i in comandos:
			#separo cada comando pelo espaço
			aux = i.split(' ')	
			
			lista_aux =  aux[1:-1] 
			#pego o ultimo elemendo do comendo e separo pelo ;
			ultimo_elemento = aux[len(aux) - 1].split(';')
			#depois de separar o ultimo comendo pego o primeiro elemento
			lista_aux.append( ultimo_elemento[0] )

			for j in range(len(lista_aux)):
				lista_aux[j] = int(lista_aux[j])

			self.comandos.append({'algoritmo': aux[0], 'lista': lista_aux})

	def monta_grafo(self):
		self.grafo['vertices'] = self.vertices 
		self.grafo['arestas'] = self.arestas
		self.grafo['eh_digrafo'] = True if self.eh_digrafo.lower() == 't' else False #Ternário, retorna True se t (TRUE) e False caso contrario
		self.grafo['tem_peso']  = True if self.tem_peso.lower() == 't' else False
		self.grafo['comandos'] = self.comandos

	#função que ler o arquivo de entrada
	def ler_entrada(self):
		dados = self.ler_arquivo()
		dados_distribuidos = self.distribui_dados(dados)
		self.pega_vertices(dados_distribuidos['grafo'])
		self.pega_arestas(dados_distribuidos['arestas'])
		self.monta_grafo()
		self.pega_comandos(dados_distribuidos['comandos'])

		return self.grafo
		
	#função que grava a resposta no arquivo de saida
	def grava_saida(self, algoritmo, resposta):

		arq = self.abrir_arquivo(self.arquivo_saida, "a")

		try:

			if algoritmo == "distancia":
				self.grava_distancia(arq, resposta)
			if algoritmo == "caminho":
				pass
			if algoritmo == "largura":
				self.grava_busca_largura(arq, resposta)
			if algoritmo == "profundidade":
				self.grava_busca_profundidade(arq, resposta)

		except:

			return False
			

		arq.close()

	def grava_distancia(self, arquivo, resposta):
		arquivo.write('DISTANCIA ')
		for i in resposta['caminho']:
			arquivo.write('%s ' % str(i))
		arquivo.write('\n')
		arquivo.write(str(resposta['distancia']))
		arquivo.write('\n\n')

	def grava_busca_largura(self, arquivo, resposta):
		
		arquivo.write('LARGURA ')

		for i in resposta['vertices']:
			arquivo.write('%s ' % str(i))

		arquivo.write('\n')

		for i in resposta['resposta']:
			for j in i:
				arquivo.write('%s ' % str(j))
			arquivo.write('\n')
			
		arquivo.write('\n')

	def grava_busca_profundidade(self, arquivo, resposta):
		
		arquivo.write('PROFUNDIDADE ')

		for i in resposta['vertices']:
			arquivo.write('%s ' % str(i))

		arquivo.write('\n')

		for i in resposta['resposta']:
			arquivo.write('%s \n' % str(i))
			
		arquivo.write('\n')
	
	def __grava_busca_profundidade(self, arquivo, resposta):
		
		arquivo.write('PROFUNDIDADE ')

		for i in resposta['vertices']:
			arquivo.write('%s ' % str(i))

		arquivo.write('\n')

		for i in resposta['resposta']:
			for j in i:
				arquivo.write('%s ' % str(j))
			arquivo.write('\n')
			
		arquivo.write('\n')