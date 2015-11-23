# Pacotes
import unittest
import sys
# importando as pastas
sys.path.append('Models')
# importando os nossos arquivos
from Grafo import *

# dados de teste
dados_valido = {'tem_peso': True, 'arestas': [['0', '1', '10'], ['1', '2', '11'], ['0', '2', '20'], ['2', '3', '12'], ['1', '3', '13'], ['2', '0', '14']], 'eh_digrafo': True, 'comandos': [{'lista': ['0', '1', '2'], 'algoritmo': 'DISTANCIA'}, {'lista': ['0', '1', '2', '0', '2'], 'algoritmo': 'DISTANCIA'}, {'lista': ['0', '2'], 'algoritmo': 'PROFUNDIDADE'}, {'lista': ['0', '3'], 'algoritmo': 'LARGURA'}, {'lista': ['0', '3'], 'algoritmo': 'MENORCAMINHO'}], 'vertices': ['0', '1', '2', '3']}
dados_invalido = {}

# classe TDD
class TestTDD (unittest.TestCase):

	def test_monta_grafo(self):
		# teste verdadeiro
		G = Grafo(dados_valido)
		self.assertEqual(G.cria_lista_adjacencia(), True)	
		
		# testa falso
		G = Grafo(dados_invalido)	
		self.assertEqual(G.cria_lista_adjacencia(), False)

	def test_distancia(self):
		# teste verdadeiro
		G = Grafo(dados_valido)
		G.cria_lista_adjacencia()
		self.assertEqual(G.calcula_distancia(['0', '1', '2']), 21)

		# testa falso
		G = Grafo(dados_invalido)
		G.cria_lista_adjacencia()
		self.assertEqual(G.calcula_distancia(['0', '1', '2']), None)

	def test_largura(self):
		# teste verdadeiro
		G = Grafo(dados_valido)
		G.cria_lista_adjacencia()
		resposta_esperada = [['0'], ['1', '2'], ['2', '2', '3'], ['2', '3', '3'], ['3', '3']]
		self.assertEqual(G.busca_em_largura('0', '3'), resposta_esperada)

		# testa falso
		G = Grafo(dados_invalido)
		G.cria_lista_adjacencia()
		resposta_esperada = [['0']]
		self.assertEqual(G.busca_em_largura('0', '3'), resposta_esperada)

	def test_profundidade(self):
		# teste verdadeiro
		G = Grafo(dados_valido)
		G.cria_lista_adjacencia()
		resposta_esperada = [['0'], ['1', '2'], ['2', '3', '2']]
		self.assertEqual(G.busca_em_profundidade('0', '2'), resposta_esperada)

		# testa falso
		G = Grafo(dados_invalido)
		G.cria_lista_adjacencia()
		resposta_esperada = [['0']]
		self.assertEqual(G.busca_em_profundidade('0', '2'), resposta_esperada)

	def test_dijkstra(self):
		# teste verdadeiro
		G = Grafo(dados_valido)
		G.cria_lista_adjacencia()
		resposta_esperada = {'caminho': ['3', '1', '0'], 'distancia': 23}
		self.assertEqual(G.dijkstra('0', '3'), resposta_esperada)

		# testa falso
		G = Grafo(dados_invalido)
		G.cria_lista_adjacencia()
		resposta_esperada = None
		self.assertEqual(G.dijkstra('0', '3'), resposta_esperada)

	def test_prim(self):
		# teste verdadeiro
		G = Grafo(dados_valido)
		G.cria_lista_adjacencia()
		resposta_esperada = {'caminho': [['2', '3', 12], ['2', '0', 14], ['0', '1', 10]], 'distancia': 36}
		self.assertEqual(G.prim('2'), resposta_esperada)

		# testa falso
		G = Grafo(dados_invalido)
		G.cria_lista_adjacencia()
		resposta_esperada = None
		self.assertEqual(G.prim('2'), resposta_esperada)

if __name__ == '__main__':
	unittest.main()
