# -*- coding: utf-8 -*-
#pacotes nativos
import sys
import os
import time

#Modulos 
from Arquivo import *
from Grafo import *
from Erros import *


#Classe principal MAIN
class Main:

	#construtor da classe, recebe como parametro os arquivos de entrada e saida
	def __init__(self, arquivo_entrada, arquivo_saida):
		self.arquivo_entrada = arquivo_entrada
		self.arquivo_saida =  arquivo_saida
		self.arquivo = Arquivo( self.arquivo_entrada, self.arquivo_saida ) #estancia da classe Arquivo
		self.grafo = None

	#funcao que que valida os arquivos de entrada e saida
	def validar_arquivo(self):
		
		try:
			# Abro os aqruivos para garantir que não estão corrompidos
			e = open(self.arquivo_entrada, "r")
			s = open(self.arquivo_saida, "w")
			#verifica se existe conteudo no arquivo de entrada
			if len(e.readline()) == 0:
				raise Erros #lancando erro

		#tratando os erros
		except IOError:
			os.system("cls")
			print("\nArquivos de entradas invalidos ou corrompidos")
			sys.exit(0)
		except Erros as E:
			os.system("cls")
			print(E.arquivo_vazio())
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
			print("Caminho Invalido")
		else:
			dados = {"caminho": lista_caminho, "distancia": result}
			resposta = self.grava_resposta_arquivo("distancia", dados)

			if resposta != False:
				time.sleep( 2 )
				print("Calcula distancia - [ OK ]")

	#executa o algoritmo que encontra uma rota entre 2 vertices
	def encontra_caminho(self, v_origem, v_destino):
		result = self.grafo.encontra_caminho( v_origem, v_destino )
		if result == None:
			print("Caminho Invalido")
		else:
			self.grava_resposta_arquivo("caminho", result)

	#executa a lista de comandos do arquivo de entrada
	def executa_comandos(self, comandos):
		os.system("cls")
		print ("\nExecutando algoritmos: \n")
		for i in comandos:
			self.chama_funcoes(i)

		print("\nArquivo de saida criado com sucesso")


	def chama_funcoes(self, comando):
		
		if comando['algoritmo'].lower() == "distancia":
			self.calcula_distancia(comando['lista'])


#Criando objeto da classe Main e chamando os metodos
try:
	if len(sys.argv) != 3:
		raise Erros
except Erros as E:
	os.system("cls")
	print(E.argvs_invalidos())
	sys.exit(0)

#Estanciando Objeto e chamando as funções
if __name__ == "__main__":
	controller = Main( sys.argv[1], sys.argv[2] )
	controller.validar_arquivo()
	dados = controller.tratar_dados_de_entrada()
	controller.monta_grafo(dados)
	#controller.encontra_caminho(0, 3)
	#controller.calcula_distancia([0,1,2,0,1,2,3])
	controller.executa_comandos(dados['comandos'])
	