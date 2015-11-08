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
	interface = Interface(tk)

	controller = Main( sys.argv[1], sys.argv[2], interface )
	controller.validar_arquivo()
	dados = controller.tratar_dados_de_entrada()
	controller.monta_grafo(dados)
	controller.executa_comandos(dados['comandos'])

	tk.mainloop()
