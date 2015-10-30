import sys
import os

from Arquivo import *

class Main:

	"""construtor da classe"""
	def __init__(self, arquivo_entrada, arquivo_saida):
		self.arquivo_entrada = arquivo_entrada
		self.arquivo_saida =  arquivo_saida

	def tratar_arquivo(self):
		
		try:
			e = open(self.arquivo_entrada, "r")
			s = open(self.arquivo_saida, "r")
		except IOError:
			os.system("cls")
			print("\nErro ao abrir o arquivo %s" % self.arquivo_saida)
			sys.exit(0)

		arquivos = Arquivo(self.arquivo_entrada, self.arquivo_saida)
		arquivos.get_file_name()


Controller = Main( sys.argv[1], sys.argv[2] )
Controller.tratar_arquivo()