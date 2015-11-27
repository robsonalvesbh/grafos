# -*- coding: utf-8 -*-
#pacotes nativos
import sys
import os
import time

from Arquivo import *
from Grafo import *
from Interface import *

#Classe principal MAIN
class Main(object):

	#construtor da classe, recebe como parametro os arquivos de entrada e saida
	def __init__(self, interface = None, arquivo_entrada = None, arquivo_saida = None):
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
			# os.system("cls")
			print("\nArquivos de entradas invalidos ou corrompidos")
			sys.exit(0)

	#chama o metodo que ler os dados do arquivo de entrada
	def tratar_dados_de_entrada(self):
		return self.arquivo.ler_entrada()

	#chama o metodo que vai gravar as respostas no arquivo de saida
	def grava_resposta_arquivo(self, algoritmo, resposta):
		return self.arquivo.grava_saida(algoritmo, resposta)

	# #monta a lista de adjacencia
	def monta_grafo(self, dados_do_grafo):
		
		if len(dados_do_grafo) > 0:
			self.grafo = Grafo(dados_do_grafo) #instancia da classe Grafo
			self.grafo.cria_lista_adjacencia() #metodo que cria a lista de adjacencia
			return True
		else:
			return False

	#Executa algoritmo que calcula a distancia de um determinado caminho
	def calcula_distancia(self, caminho, requisicao = False):

		lista_caminho = list(caminho) #copia a lista de caminho para lista_caminho
		result = self.grafo.calcula_distancia(caminho)

		if result == None:
			if requisicao == True:
				return result
			else:
				self.interface.lista_respostas.append('Calcula distancia - [ ERROR ]')
		else:
			dados = {"caminho": lista_caminho, "distancia": result}

			if requisicao == True:
				return dados
			else:
				resposta = self.grava_resposta_arquivo("distancia", dados)

				if resposta != False:
					self.interface.lista_respostas.append('Calcula distancia - [ OK ]')

	def busca_largura(self, lista, requisicao = False):
		vertices = list(lista)
		result = self.grafo.busca_em_largura( lista[0], lista[1] )

		if result == None:
			if requisicao == True:
				return result
			else:
				self.interface.lista_respostas.append('Busca em largura  - [ ERROR ]')
		else:
			dados = {"vertices": vertices, "resposta": result}
			if requisicao == True:
				return dados
			else:
				resposta = self.grava_resposta_arquivo("largura", dados)

				if resposta != False:
					self.interface.lista_respostas.append('Busca em largura  - [ OK ]')

	def busca_profundidade(self, lista, requisicao = False):
		vertices = list(lista)
		result = self.grafo.busca_em_profundidade( lista[0], lista[1] )

		if result == None:
			if requisicao == True:
				return result
			else:
				self.interface.lista_respostas.append('Busca em profundidade  - [ ERROR ]')
		else:
			dados = {"vertices": vertices, "resposta": result}

			if requisicao == True:
				return dados
			else:
				resposta = self.grava_resposta_arquivo("profundidade", dados)

				if resposta != False:
					self.interface.lista_respostas.append('Busca em profundidade  - [ OK ]')

	def menor_caminho(self, origem, destino, requisicao = False):

		result = self.grafo.dijkstra(origem, destino)

		if result == None:
			if requisicao == True:
				return result
			else:
				self.interface.lista_respostas.append('Busca menor caminho (DIJKSTRA)  - [ ERROR ]')
		else:
			dados = {"vertices": [origem, destino], "resposta": result}

			if requisicao == True:
				return dados
			else:
				resposta = self.grava_resposta_arquivo("menorcaminho", dados)

				if resposta != False:
					self.interface.lista_respostas.append('Busca menor caminho (DIJKSTRA)  - [ OK ]')

	def gerar_prim(self, origem, requisicao = False):
		result = self.grafo.prim( origem )

		if result == None:
			if requisicao == True:
				return result
			else:
				self.interface.lista_respostas.append('Prim - [ ERROR ]')
		else:
			dados = {"vertices": origem, "resposta": result}

			if requisicao == True:
				return dados
			else:
				print(dados)
				resposta = self.grava_resposta_arquivo("prim", dados)

				if resposta != False:
					self.interface.lista_respostas.append('Prim - [ OK ]')
		
	#executa a lista de comandos do arquivo de entrada
	def executa_comandos(self, comandos):

		for i in comandos:
			self.chama_funcoes(i)

		print("Executando...")

	def chama_funcoes(self, comando, requisicao = False):

		if (requisicao == True):
			if comando['algoritmo'].lower() == "distancia":
				return self.calcula_distancia(comando['lista'], True)

			if comando['algoritmo'].lower() == "largura":
				return self.busca_largura(comando['lista'], True)

			if comando['algoritmo'].lower() == "profundidade":
				return self.busca_profundidade(comando['lista'], True)

			if comando['algoritmo'].lower() == "menorcaminho":
				return self.menor_caminho(comando['lista'][0], comando['lista'][1], True)

			if comando['algoritmo'].lower() == "prim":
				return self.gerar_prim(comando['lista'][0], True)
		else:

			if comando['algoritmo'].lower() == "distancia":
				return self.calcula_distancia(comando['lista'])

			if comando['algoritmo'].lower() == "largura":
				return self.busca_largura(comando['lista'])

			if comando['algoritmo'].lower() == "profundidade":
				return self.busca_profundidade(comando['lista'])

			if comando['algoritmo'].lower() == "menorcaminho":
				return self.menor_caminho(comando['lista'][0], comando['lista'][1])

			if comando['algoritmo'].lower() == "prim":
				return self.gerar_prim(comando['lista'][0])

