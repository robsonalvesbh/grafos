# -*- coding: utf-8 -*-
#pacotes nativos
import sys
import os
import time

# #Modulos 
# from Arquivo import *
# from Grafo import *
from Arquivo import *
from Grafo import *
from Interface import *

#Classe principal MAIN
class Main(object):

	#construtor da classe, recebe como parametro os arquivos de entrada e saida
	def __init__(self, arquivo_entrada, arquivo_saida, interface):
		self.arquivo_entrada = arquivo_entrada
		self.arquivo_saida =  arquivo_saida
		self.arquivo = Arquivo( self.arquivo_entrada, self.arquivo_saida ) #estancia da classe Arquivo
		self.grafo = None
		self.interface = interface

	#funcao que que valida os arquivos de entrada e saida
	def validar_arquivo(self):
		
		try:
			# Abro os aqruivos para garantir que não estão corrompidos
			e = open(self.arquivo_entrada, "r")
			s = open(self.arquivo_saida, "w")
			#verifica se existe conteudo no arquivo de entrada
			if len(e.readline()) == 0:
				raise IOError

		#tratando os erros
		except IOError:
			os.system("cls")
			print("\nArquivos de entradas invalidos ou corrompidos")
			sys.exit(0)

	#chama o metodo que ler os dados do arquivo de entrada
	def tratar_dados_de_entrada(self):
		return self.arquivo.ler_entrada()

	#chama o metodo que vai gravar as respostas no arquivo de saida
	def grava_resposta_arquivo(self, algoritmo, resposta):
		return self.arquivo.grava_saida(algoritmo, resposta)

	#monta a lista de adjacencia
	def monta_grafo(self, dados):
		self.grafo = Grafo(dados) #instancia da classe Grafo
		self.grafo.cria_lista_adjacencia() #metodo que cria a lista de adjacencia

	#Executa algoritmo que calcula a distancia de um determinado caminho
	def calcula_distancia(self, caminho):
		lista_caminho = list(caminho) #copia a lista de caminho para lista_caminho
		result = self.grafo.calcula_distancia(caminho)

		if result == None:
			self.interface.lista_respostas.append('Calcula distancia - [ ERROR ]')
		else:
			dados = {"caminho": lista_caminho, "distancia": result}
			resposta = self.grava_resposta_arquivo("distancia", dados)

			if resposta != False:
				self.interface.lista_respostas.append('Calcula distancia - [ OK ]')

	#executa o algoritmo que encontra uma rota entre 2 vertices
	def encontra_caminho(self, v_origem, v_destino):
		result = self.grafo.encontra_caminho( v_origem, v_destino )
		if result == None:
			print("Caminho Invalido")
		else:
			self.grava_resposta_arquivo("caminho", result)

	def busca_largura(self, lista):
		vertices = list(lista)
		result = self.grafo.busca_em_largura( lista[0], lista[1] )
		if result == None:
			self.interface.lista_respostas.append('Busca em largura  - [ ERROR ]')
		else:
			dados = {"vertices": vertices, "resposta": result}
			resposta = self.grava_resposta_arquivo("largura", dados)

			if resposta != False:
				self.interface.lista_respostas.append('Busca em largura  - [ OK ]')

	def busca_profundidade(self, lista):
		vertices = list(lista)
		result = self.grafo.busca_em_profundidade( lista[0], lista[1] )
		if result == None:
			self.interface.lista_respostas.append('Busca em profundidade  - [ ERROR ]')
		else:
			dados = {"vertices": vertices, "resposta": result}
			resposta = self.grava_resposta_arquivo("profundidade", dados)

			if resposta != False:
				self.interface.lista_respostas.append('Busca em profundidade  - [ OK ]')

	def menor_caminho(self, origem, destino):

		result = self.grafo.dijkstra(origem, destino)

		if result == None:
			self.interface.lista_respostas.append('Busca menor caminho (DIJKSTRA)  - [ ERROR ]')
		else:
			dados = {"vertices": [origem, destino], "resposta": result}
			resposta = self.grava_resposta_arquivo("menorcaminho", dados)

			if resposta != False:
				self.interface.lista_respostas.append('Busca menor caminho (DIJKSTRA)  - [ OK ]')

	#executa a lista de comandos do arquivo de entrada
	def executa_comandos(self, comandos):
		os.system("cls")

		for i in comandos:
			self.chama_funcoes(i)

		print("Executando...")

	def chama_funcoes(self, comando):
		
		if comando['algoritmo'].lower() == "distancia":
			self.calcula_distancia(comando['lista'])

		if comando['algoritmo'].lower() == "largura":
			self.busca_largura(comando['lista'])

		if comando['algoritmo'].lower() == "profundidade":
			self.busca_profundidade(comando['lista'])

		if comando['algoritmo'].lower() == "menorcaminho":
			v = comando['lista']
			self.menor_caminho(v[0], v[1])

