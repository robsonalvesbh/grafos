import networkx as nx
import matplotlib.pyplot as plt
from tkinter import *

from Controllers.Main import *
from Index import *

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

		#  botao gera arquivo
		self.btnExec = Button(self.ArquivoFrame)
		self.btnExec['text'] = 'Gerar arquivo de saida'
		self.formata_button(self.btnExec,'#2C82C9')
		self.btnExec['command'] = self.algoritmos
		self.btnExec.pack(side = LEFT)

		# botao cria grafo
		self.btnCreate = Button(self.ArquivoFrame)
		self.btnCreate['text'] = 'Criar grafo'
		self.formata_button(self.btnCreate,'#2969B0')
		self.btnCreate['command'] = self.criar_grafo
		self.btnCreate.pack(side = LEFT)

		# resultado leitura arquivo
		self.algoritmosFrame = Frame(instancia)
		self.algoritmosFrame['pady'] = '15'
		self.algoritmosFrame['bg'] = BACKGROUND
		self.algoritmosFrame.pack()

		#container para criação do grafo
		self.grafoCreateFrame = Frame(instancia, bg = BACKGROUND, pady = '10')

		# frames
		self.verticesFrame = Frame(self.grafoCreateFrame, bg = BACKGROUND)
		self.arestasFrame = Frame(self.grafoCreateFrame, bg = BACKGROUND)
		self.digrafoFrame = Frame(self.grafoCreateFrame, bg = BACKGROUND)
		self.pesoFrame = Frame(self.grafoCreateFrame, bg = BACKGROUND)
		self.btnCriaGrafo = Frame(self.grafoCreateFrame, bg = BACKGROUND, pady = '15')

		# vertices
		self.verticesLabel = Label(self.verticesFrame, text = "Vertices: ", bg = BACKGROUND)
		self.vertices = Entry(self.verticesFrame, bg = BACKGROUND)
		self.vertices.insert(0, "1 2 3")
		self.formata_entrada(self.vertices)

		self.verticesLabel.pack()
		self.vertices.pack()

		# arestas
		self.arestaLabel = Label(self.arestasFrame, text = "Aresta: ", bg = BACKGROUND)
		self.aresta = Entry(self.arestasFrame, bg = BACKGROUND)
		self.aresta.insert(0, "[1 2 30], [2 3 10]")
		self.formata_entrada(self.aresta)

		self.arestaLabel.pack()
		self.aresta.pack()

		# digrafo
		self.digrafoLabel = Label(self.digrafoFrame, text = "Digrafo: ", bg = BACKGROUND)
		self.digrafo = Entry(self.digrafoFrame, bg = BACKGROUND)
		self.digrafo.insert(0, "True")
		self.formata_entrada(self.digrafo)

		self.digrafoLabel.pack()
		self.digrafo.pack()

		# peso
		self.pesoLabel = Label(self.pesoFrame, text = "Peso: ", bg = BACKGROUND)
		self.peso = Entry(self.pesoFrame, bg = BACKGROUND)
		self.peso.insert(0, "True")
		self.formata_entrada(self.peso)

		self.pesoLabel.pack()
		self.peso.pack()

		# botao cria grafo
		self.btnGeraGrafo = Button(self.btnCriaGrafo)
		self.btnGeraGrafo['text'] = 'Gerar Grafo'
		self.formata_button(self.btnGeraGrafo,'#FAC51C')
		self.btnGeraGrafo['command'] = self.gera_grafo

		# empacotando os frames
		self.verticesFrame.pack()
		self.arestasFrame.pack()
		self.digrafoFrame.pack()
		self.pesoFrame.pack()
		self.btnCriaGrafo.pack()

		# lista de respostas
		self.lista_respostas = []

	def janela(self, instancia):
		instancia.geometry("600x400")
		instancia.title('Grafos')
		instancia['bg'] = BACKGROUND

	def setDados(self, dados):
		self.dados = dados

	def algoritmos(self):

		if self.grafoCreateFrame.winfo_ismapped():
			self.grafoCreateFrame.pack_forget()
			self.algoritmosFrame.pack()
		else:
			self.algoritmosFrame.pack()
			self.grafoCreateFrame.pack_forget()

		self.exibe_algoritmos()

	def exibe_algoritmos(self):

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
			arq['fg'] = '#00A885'
			arq['font'] = ('Helvetica', '16')
			arq.pack()

			self.btnExec['text'] = 'Desenhar o Grafo'
			self.btnExec['bg'] = '#00A885'
			self.btnExec['command'] = self.plotar_grafo

	def plotar_grafo(self):

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

	def criar_grafo(self):
		
		if self.algoritmosFrame.winfo_ismapped():
			self.algoritmosFrame.pack_forget()
			self.grafoCreateFrame.pack()
			self.btnGeraGrafo.pack()
		else:
			self.grafoCreateFrame.pack_forget()
			self.algoritmosFrame.pack()

	def formata_button(self, button, color = None):

		button['bd'] = 0
		button['width'] = 30
		button['height'] = 3
		button['fg'] = '#fff'
		button['bg'] = color

	def formata_entrada(self, entrada):
		entrada['width'] = 72

	def gera_grafo(self):

		grafo = {}

		grafo['vertices'] = self.vertices.get().split(' ')
		grafo['arestas'] = self.formata_dados(self.aresta.get().split(', '))
		grafo['eh_digrafo'] = bool( self.digrafo.get() )
		grafo['tem_peso']  = bool( self.peso.get() )

		newGrafo = Main()
		newGrafo.monta_grafo(grafo)
		self.dados = grafo

		self.btnExec['text'] = 'Desenhar o Grafo'
		self.btnExec['bg'] = '#00A885'
		self.btnExec['command'] = self.plotar_grafo

	def formata_dados(self, dados):
		
		novos_dados = []
		
		for i in dados:
			novos_dados.append(i[1:-1].split(' '))

		return novos_dados
		