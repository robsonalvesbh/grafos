class Arquivo(object):

	"""Método construtor da classe"""
	def __init__(self, arquivo_entrada, arquivo_saida):
		self.arquivo_entrada = arquivo_entrada
		self.arquivo_saida = arquivo_saida
	
	def get_file_name(self):
		print("O nome do arquivo de entrada e %s " % self.arquivo_entrada)
		print("E o arquivo de saida e %s" % self.arquivo_saida)