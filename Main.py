import sys
import os

from Arquivo import *
from Grafo import *
from Erros import *


#Inicio da classe main
class Main:

	#construtor da classe
	def __init__(self, arquivo_entrada, arquivo_saida):
		self.arquivo_entrada = arquivo_entrada
		self.arquivo_saida =  arquivo_saida
		self.arquivo = Arquivo(self.arquivo_entrada, self.arquivo_saida)
		self.grafo = None

	def validar_arquivo(self):
		
		try:
			# Abro os aqruivos para garantir que não estão corrompidos
			e = open(self.arquivo_entrada, "r")
			s = open(self.arquivo_saida, "w")
			
			if len(e.readline()) == 0:
				raise Erros

		except IOError:
			os.system("cls")
			print("\nArquivos de entradas invalidos ou corrompidos")
			sys.exit(0)
		except Erros as E:
			os.system("cls")
			print(E.arquivo_vazio())
			sys.exit(0)

	def tratar_dados_de_entrada(self):
		return self.arquivo.ler_entrada()

	def grava_resposta_arquivo(self, algoritmo, resposta):
		self.arquivo.grava_saida(algoritmo, resposta)

	def monta_grafo(self, dados):
		self.grafo = Grafo(dados)
		self.grafo.cria_lista_adjacencia()

	def calcula_distancia(self, caminho):
		lista_caminho = list(caminho)
		result = self.grafo.calcula_distancia(caminho)

		if result == None:
			print("Caminho Invalido")
		else:
			dados = {"caminho": lista_caminho, "distancia": result}
			self.grava_resposta_arquivo("distancia", dados)

	def encontra_caminho(self, v_origem, v_destino):
		result = self.grafo.encontra_caminho( v_origem, v_destino )
		if result == None:
			print("Caminho Invalido")
		else:
			self.grava_resposta_arquivo("caminho", result)

	def executa_comandos(self, comandos):
		
		for i in comandos:
			self.chama_funcoes(i)

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
	controller.encontra_caminho(0, 3)
	#controller.calcula_distancia([0,1,2,0,1,2,3])
	controller.executa_comandos(dados['comandos'])
	