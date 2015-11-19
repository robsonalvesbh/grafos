from tkinter import *
import networkx as nx
import matplotlib.pyplot as plt


BACKGROUND = '#F9F9F9'

class Interface(object):

	def __init__(self, instancia):
		
		# dados do grafo
		self.dados = None

		#configurações da janeça
		self.janela(instancia)

		# frame do titulo
		self.titleFrame = Frame(instancia)
		self.titleFrame.pack()

		self.title = Label(self.titleFrame)
		self.title['text'] = 'Trabalho de Grafos'
		self.title['font'] = ('Helvetica', '20')
		self.title['fg'] = '#666'
		self.title['pady'] = '15'
		self.title['bg'] = BACKGROUND
		self.title.pack()

		# frame do botão gerar aquivo
		self.ArquivoFrame = Frame(instancia)
		self.ArquivoFrame['bg'] = BACKGROUND
		self.ArquivoFrame['pady'] = '10'
		self.ArquivoFrame.pack()

		self.btnExec = Button(self.ArquivoFrame)
		self.btnExec['text'] = 'Gerar arquivo de saida'
		self.btnExec['command'] = self.algoritmos
		self.btnExec['width'] = 30
		self.btnExec['height'] = 3
		self.btnExec['bd'] = 0
		self.btnExec['fg'] = '#fff'
		self.btnExec['bg'] = '#2C82C9'
		self.btnExec.pack(side = LEFT)

		self.btnCreate = Button(self.ArquivoFrame)
		self.btnCreate['text'] = 'Criar grafo'
		self.btnCreate['width'] = 30
		self.btnCreate['height'] = 3
		self.btnCreate['bd'] = 0
		self.btnCreate['fg'] = '#fff'
		self.btnCreate['bg'] = '#2969B0'
		self.btnCreate.pack(side = LEFT)

		# resultado leitura arquivo
		self.algoritmosFrame = Frame(instancia)
		self.algoritmosFrame['pady'] = '15'
		self.algoritmosFrame['bg'] = BACKGROUND
		self.algoritmosFrame.pack()

		# lista de respostas
		self.lista_respostas = []

	def janela(self, instancia):
		instancia.geometry("600x400")
		instancia.title('Grafos')
		instancia['bg'] = BACKGROUND

	def setDados(self, dados):
		self.dados = dados

	def algoritmos(self):
		
		if len(self.lista_respostas) > 0:
			alg = Label(self.algoritmosFrame)
			alg['bg'] = BACKGROUND
			alg['text'] = self.lista_respostas.pop(0)
			alg.pack()
			self.algoritmosFrame.after(1000, self.algoritmos)
		else:
			arq = Label(self.algoritmosFrame)
			arq['bg'] = BACKGROUND
			arq['pady'] = "15"
			arq['text'] = "Arquivo de saida gerado com sucesso!"
			arq['fg'] = 'green'
			arq['font'] = ('Helvetica', '16')
			arq.pack()

			self.btnExec['text'] = 'Desenhar o Grafo'
			self.btnExec['bg'] = '#00A885'
			self.btnExec['command'] = self.plotar_grafo

	def plotar_grafo (self):

		# verifica se é um grafo direcionado ou não
		if self.dados['eh_digrafo'] == True:
			G = nx.DiGraph()
		else:
			G = nx.Graph()
		
		# Adiciona os vertices ao grafo
		G.add_nodes_from(self.dados['vertices'])

		# Adiciona as arestas
		for aresta in self.dados['arestas']:
			G.add_edge(aresta[0],aresta[1],weight=aresta[2])

		# desenha e exibe
		nx.draw_networkx(G)
		plt.show()