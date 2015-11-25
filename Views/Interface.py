import networkx as nx
import matplotlib.pyplot as plt
from tkinter import *

from Controllers.Main import *

BACKGROUND = '#F9F9F9'

class Interface(object):

	def __init__(self, instancia, exibe_gera_arquivo = True):
		
		self.controller = None
		self.controller_da_interface = Main()
		# dados do grafo
		self.dados_do_arquivo = None
		self.dados_da_interface = None

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
		if exibe_gera_arquivo == True:
			self.btnExec.pack(side = LEFT)

		#  botao quadro comandos
		self.btnComandos = Button(self.ArquivoFrame)
		self.btnComandos['text'] = 'Executar algoritmos'
		self.formata_button(self.btnComandos,'#2C82C9')
		self.btnComandos['command'] = self.quadro_comandos

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

		# frame dos comandos
		self.comandosAlgoritmosFrame = Frame(instancia, bg = BACKGROUND, pady = '10')

		# frames comandos
		self.boxAreaComandos = Frame(self.comandosAlgoritmosFrame, bg = BACKGROUND)
		self.frameBtninformarComandos = Frame(self.comandosAlgoritmosFrame, bg = BACKGROUND, pady = '15')

		self.LabelAreaComandos = Label(self.boxAreaComandos, text = "COMANDOS: ", bg = BACKGROUND)
		self.AreaComandos = Text(self.boxAreaComandos, bg = '#f1f1f1', width = '68', height = '10')

		self.LabelAreaComandos.pack()
		self.AreaComandos.pack()

		self.btnInformarComandos = Button(self.frameBtninformarComandos)
		self.btnInformarComandos['text'] = 'Executar os comandos'
		self.formata_button(self.btnInformarComandos,'#FAC51C')
		self.btnInformarComandos['command'] = self.recebe_comando

		self.boxAreaComandos.pack()
		self.btnInformarComandos.pack()

		# lista de respostas
		self.lista_respostas = []	

	def janela(self, instancia):
		instancia.geometry("1100x500")
		instancia.title('Grafos')
		instancia['bg'] = BACKGROUND

	def setDados(self, dados):
		self.dados_do_arquivo = dados

	def setController(self, objeto):
		self.controller = objeto

	def monta_o_grafo_do_arquivo(self):
		self.controller.monta_grafo(self.dados_do_arquivo)

	def monta_o_grafo_da_interface(self):
		self.controller_da_interface.monta_grafo(self.dados_da_interface)
		
	def chama_as_funcoes(self, comandos):
		self.controller.executa_comandos(comandos)

	def algoritmos(self):
		
		self.monta_o_grafo_do_arquivo()

		self.chama_as_funcoes(self.dados_do_arquivo['comandos'])

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
			self.algoritmosFrame.after(1000, self.exibe_algoritmos)
		else:
			arq = Label(self.algoritmosFrame)
			arq['bg'] = BACKGROUND
			arq['pady'] = "15"
			arq['text'] = "Arquivo de saida gerado com sucesso!"
			arq['fg'] = '#00A885'
			arq['font'] = ('Helvetica', '16')
			arq.pack()

			self.btnExec['text'] = 'Desenhar o Grafo do Arquivo'
			self.btnExec['bg'] = '#00A885'
			self.btnExec['command'] = self.plotar_grafo_arquivo

		return True

	def plotar_grafo_arquivo(self):
		self.plotar_grafo(self.dados_do_arquivo)

	def plotar_grafo_interface(self):
		self.plotar_grafo(self.dados_da_interface)

	def plotar_grafo(self, grafo):

		lista_labels = []
		lista_peso = []
		node_size = 1600 
		node_color = 'red'
		node_alpha = 1
		node_text_size = 12
		edge_color = "blue" 
		edge_alpha = 0.3 
		edge_tickness = 1
		edge_text_pos = 0.3
		text_font = 'sans-serif'

		# verifica se é um grafo direcionado ou não
		if grafo['eh_digrafo'] == 'True':
			G = nx.DiGraph()
		else:
			G = nx.Graph()
		
		# Adiciona os vertices ao grafo
		G.add_nodes_from(grafo['vertices'])

		# Adiciona as arestas
		for aresta in grafo['arestas']:
			G.add_edge(aresta[0],aresta[1])
			lista_labels.append((aresta[0],aresta[1]))
			lista_peso.append(aresta[2])

		graph_pos = nx.shell_layout(G)		
		nx.draw_networkx_edges(G,graph_pos)

		nx.draw_networkx_nodes(G,graph_pos,node_size=node_size, alpha=node_alpha, node_color=node_color)
		nx.draw_networkx_edges(G,graph_pos,width=edge_tickness, alpha=edge_alpha,edge_color=edge_color)
		nx.draw_networkx_labels(G, graph_pos,font_size=node_text_size, font_family=text_font)

		if grafo['tem_peso'] == 'True':
			edge_labels = dict(zip(lista_labels, lista_peso))
			nx.draw_networkx_edge_labels(G, graph_pos, edge_labels=edge_labels, label_pos=edge_text_pos)

		# desenha e exibe
		# nx.draw_networkx(G)
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
		grafo['eh_digrafo'] =  self.digrafo.get() 
		grafo['tem_peso']  =  self.peso.get() 

		print(grafo)
		
		self.dados_da_interface = grafo
		self.monta_o_grafo_da_interface()

		self.btnComandos.pack(side = LEFT)
		self.btnCreate['text'] = 'Desenhar o Grafo'
		self.btnCreate['bg'] = '#E14938'
		self.btnCreate['command'] = self.plotar_grafo_interface

	def formata_dados(self, dados):
		
		novos_dados = []
		
		for i in dados:
			novos_dados.append(i[1:-1].split(' '))

		return novos_dados
		
	def quadro_comandos(self):
		if self.algoritmosFrame.winfo_ismapped() or self.grafoCreateFrame.winfo_ismapped():
			self.algoritmosFrame.pack_forget()
			self.grafoCreateFrame.pack_forget()
			self.comandosAlgoritmosFrame.pack()
			self.frameBtninformarComandos.pack()
		else:
			self.comandosAlgoritmosFrame.pack_forget()
			self.algoritmosFrame.pack()
			self.grafoCreateFrame.pack()

	def recebe_comando(self):

		lista_de_comandos = []
		comandos = self.AreaComandos.get("1.0",END).split('\n')

		for comando in comandos:

			if comando != '':
				comando = comando.split(' ')
				lista_aux = comando[1:]
				lista_de_comandos.append( {'algoritmo': comando[0], 'lista': lista_aux} )

		for i in lista_de_comandos:
			print(self.controller_da_interface.chama_funcoes(i, True))




		