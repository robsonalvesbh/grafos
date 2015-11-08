from tkinter import *
import time

BACKGROUND = '#F9F9F9'

class Interface(object):

	def __init__(self, instancia):
		
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
		# self.btnExec.bind("<Button-1>", self.algoritmos)
		self.btnExec['width'] = 40
		self.btnExec['height'] = 3
		self.btnExec['bg'] = BACKGROUND
		self.btnExec.pack()

		self.algoritmosFrame = Frame(instancia)
		self.algoritmosFrame['pady'] = '15'
		self.algoritmosFrame['bg'] = BACKGROUND
		self.algoritmosFrame.pack()

		self.lista_respostas = []

	def janela(self, instancia):
		instancia.geometry("600x350")
		instancia.title('Grafos')
		instancia['bg'] = BACKGROUND

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
