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

URL_ROOT = "D:\wamp\www\grafos\img"

app = Flask(__name__)

controller_da_api = Main()

@app.route('/')
def hello_world():
    return 'BIENVENIDO EN LA BIBLIOTECA DE GRAFO'

@app.route('/criaGrafo', methods=['POST'])
def criaGrafo():

	grafo = request.data
	grafo = json.loads(grafo)
	controller_da_api.monta_grafo(grafo)
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

def plotar_grafo(grafo):

	lista_labels = []
	lista_peso = []
	node_size = 1600 
	node_color = 'red'
	node_alpha = 1
	node_text_size = 12
	edge_color = "blue" 
	edge_alpha = 0.3 
	edge_tickness = 1
	edge_text_pos = 0.3
	text_font = 'sans-serif'

	# verifica se é um grafo direcionado ou não
	if grafo['eh_digrafo'] == 'True':
		G = nx.DiGraph()
	else:
		G = nx.Graph()
	
	# Adiciona os vertices ao grafo
	G.add_nodes_from(grafo['vertices'])

	# Adiciona as arestas
	for aresta in grafo['arestas']:
		G.add_edge(aresta[0],aresta[1])
		lista_labels.append((aresta[0],aresta[1]))
		lista_peso.append(aresta[2])

	graph_pos = nx.shell_layout(G)		
	nx.draw_networkx_edges(G,graph_pos)

	nx.draw_networkx_nodes(G,graph_pos,node_size=node_size, alpha=node_alpha, node_color=node_color)
	nx.draw_networkx_edges(G,graph_pos,width=edge_tickness, alpha=edge_alpha,edge_color=edge_color)
	nx.draw_networkx_labels(G, graph_pos,font_size=node_text_size, font_family=text_font)

	if grafo['tem_peso'] == 'True':
		edge_labels = dict(zip(lista_labels, lista_peso))
		nx.draw_networkx_edge_labels(G, graph_pos, edge_labels=edge_labels, label_pos=edge_text_pos)

	now = datetime.now()
	name =  "grafo_" + str(now.day) + "_" + str(now.month) + "_" + str(now.hour) + "_" + str(now.minute) + "_" + str(now.second) +".png"
	plt.savefig(URL_ROOT + '\\' + name)

	return name

@app.route('/distancia/<caminho>')
def distancia(caminho):

	caminho = caminho.split('-')
	return json.dumps( controller_da_api.calcula_distancia(caminho, True) )

@app.route('/largura/<vertices>')
def largura(vertices):
	v = vertices.split('-')
	return json.dumps( controller_da_api.busca_largura(v, True) )

@app.route('/profundidade/<vertices>')
def profundidade(vertices):
	v = vertices.split('-')
	return json.dumps( controller_da_api.busca_profundidade(v, True) )

@app.route('/prim/<origem>')
def prim(origem):
	return json.dumps( controller_da_api.gerar_prim(origem, True) )

@app.route('/dijkstra/<origem>/<destino>')
def dijkstra(origem, destino):
	return json.dumps( controller_da_api.menor_caminho(origem, destino, True) )

if __name__ == '__main__':
	app.run(debug=True)