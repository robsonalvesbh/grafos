import sys
import os
import unittest

from Arquivo import *
from Erros import *


"""Inicio da classe main"""
class Main:

	"""construtor da classe"""
	def __init__(self, arquivo_entrada, arquivo_saida):
		self.arquivo_entrada = arquivo_entrada
		self.arquivo_saida =  arquivo_saida

	def tratar_arquivo(self):
		
		try:

			e = open(self.arquivo_entrada, "r")
			s = open(self.arquivo_saida, "r")
			
			if len(e.readline()) == 0:
				raise Erros

			e.close()
			s.close()
				
		except IOError:
			os.system("cls")
			print("\nErro ao abrir o arquivo %s" % self.arquivo_saida)
			sys.exit(0)
		except Erros as E:
			os.system("cls")
			print(E.arquivo_vazio())
			sys.exit(0)

		arquivos = Arquivo(self.arquivo_entrada, self.arquivo_saida)
		arquivos.get_file_name()

"""Fim da classe Main"""

"""Criando objeto da classe Main e chamando os metodos"""
try:

	if len(sys.argv) != 3:
		raise Erros

except Erros as E:
	os.system("cls")
	print(E.argvs_invalidos())
	sys.exit(0)

Controller = Main( sys.argv[1], sys.argv[2] )
Controller.tratar_arquivo()