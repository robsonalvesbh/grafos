import sys
import json
import networkx as nx
import matplotlib.pyplot as plt
from flask import *
from datetime import datetime

sys.path.insert(0, '../')
sys.path.insert(0, '../Controllers/')
sys.path.insert(0, '../Models/')
sys.path.insert(0, '../Views/')

from Main import *

URL_ROOT = "C:\\Users\\robso\Projetos\\trabalho_fernando\\imagens_grafos\\"

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'TESTANDO MINHA API'

@app.route('/criaGrafo', methods=['POST'])
def criaGrafo():

	grafo = {}

	grafo['vertices'] = request.form['vertices'].split(' ')
	grafo['arestas'] = formata_dados(request.form['arestas'].split(', '))
	grafo['eh_digrafo'] =  request.form['digrafo'] 
	grafo['tem_peso']  = request.form['peso']

	resposta = {}
	resposta['status'] = 200 
	resposta['mensagem'] = "Requisição realizada com sucesso"
	resposta['grafo'] = plotar_grafo(grafo)

	return json.dumps( resposta )

def formata_dados(dados):
	
	novos_dados = []

	for i in dados:
		novos_dados.append(i[1:-1].split(' '))

	return novos_dados

def plotar_grafo(dados):

	# verifica se é um grafo direcionado ou não
	if dados['eh_digrafo'] == True:
		G = nx.DiGraph()
	else:
		G = nx.Graph()
	
	G.clear()

	# Adiciona os vertices ao grafo
	G.add_nodes_from(dados['vertices'])

	# Adiciona as arestas
	for aresta in dados['arestas']:
		G.add_edge(aresta[0],aresta[1],weight=aresta[2])

	# desenha e exibe
	nx.draw_networkx(G)
	now = datetime.now()
	name = URL_ROOT + "grafo_" + str(now.day) + "_" + str(now.month) + "_" + str(now.hour) + "_" + str(now.minute) + ".png"
	plt.savefig(name)

	return name


@app.route('/test')
def teste():
	t = Teste()
	a = t.show()
	return a

if __name__ == '__main__':
	app.run(debug=True)