import sys
import os

from Arquivo import *
from Erros import *


"""Inicio da classe main"""
class Main:

	"""construtor da classe"""
	def __init__(self, arquivo_entrada, arquivo_saida):
		self.arquivo_entrada = arquivo_entrada
		self.arquivo_saida =  arquivo_saida

	def validar_arquivo(self):
		
		try:
			""" Abro os aqruivos para garantir que não estão corrompidos"""
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
		arquivos = Arquivo(self.arquivo_entrada, self.arquivo_saida)
		arquivos.ler_entrada()


""" Criando objeto da classe Main e chamando os metodos """
try:
	if len(sys.argv) != 3:
		raise Erros
except Erros as E:
	os.system("cls")
	print(E.argvs_invalidos())
	sys.exit(0)

""" Estanciando Objeto e chamando as funções"""

Controller = Main( sys.argv[1], sys.argv[2] )
Controller.validar_arquivo()
Controller.tratar_dados_de_entrada()
