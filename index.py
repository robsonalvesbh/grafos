# -*- coding: utf-8 -*-

# Pacotes
import sys

# importando as pastas
sys.path.append('Controllers')
sys.path.append('Models')
sys.path.append('Views')

# importando os nossos arquivos
from Main import *

#Estanciando Objeto e chamando as funções
if __name__ == "__main__":

	tk = Tk()

	if len(sys.argv) == 3:
		interface = Interface(tk, True)
		controller = Main( interface, sys.argv[1], sys.argv[2] )
		controller.validar_arquivo()
		dados = controller.tratar_dados_de_entrada()
	elif len(sys.argv) == 1:
		interface = Interface(tk, False)
		controller = Main( interface )
		dados = None
	else:
		print('É necessário passar o arquivo de entrada e saida')
		sys.exit(0)

	interface.setController(controller)
	interface.setDados(dados)

	tk.mainloop()
