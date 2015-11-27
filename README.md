Trabalho de Teoria da Computação
=================================================

Grafos
------

Projeto apresentado à disciplina de Teoria da Computação do curso de Ciência da Computação Pitágoras Betim.

Orientador: [Fernando Braz](https://github.com/fernandoafb)

## Integrantes deste projeto:

* [Robson Alves](https://github.com/robsonalvesbh)
* Marcela Fernandes
* Isaac Oliveira
* Junio Almeida
* Dhéssika Gomes

## Linguagem Utilizada

* Python 3.5.0

## Bibliotecas utilizadas

* Numpy
* Matplotlib
* Networkx
* Numpy
* Coverage
* Unittest

Todas as blibliotecas foram instaladas utilizando o gerenciador de dependencias do Python, o PIP.

Existe um arquivo na raiz do projeto chamado requirements.txt e nele contém todas as bibliotecas do python, para instalar as bibliotecas basta através do Prompt de Comando você navegar até a pasta raiz do projeto e executar o seguinte comando:

> pip install -r requirements.txt

## Neste projeto foi implementado os seguintes algoritmos:

### Calculo de distancia

Você passa um determinado caminho e o algoritmo retornará a distância percorrida.

### Busca em Largura

Com esse algoritmo é possivel fazer busca em um grafo partindo de um vértice origem, ele percorre seus vizinhos até encontrar o vértice 
desejado. Ele pode ser usado para verificar a conectividade entre os vétices do grafo e também para verificar se um grafo é biparte.

### Busca em Profundidade

Com esse algoritmo é possivel fazer busca em um grafo partindo de um vértice origem, percorrendo todos os vertices de seu ramo, até encontrar
o vertice desejado. Ele é usado para solucionar problemas como o de labirinto e de quebra cabeça. 

### Dijkstra

É um algoritmo usado para identificar qual o menor caminho dentro de um grafo. Ele é utilizado por exemplo para definir 
qual o menor caminho entre duas cidades, como Belo Horizonte e São Paulo.

### Prim

A partir de um vertice de origem ele retornará uma arvoré geradora minima.

## Classes Utilizadas

* Class Arquivo

Dentro dessa classe, encontra-se as funções responsaveis por abrir, ler e gravar em cada variavel os dados contidos no arquivo de entrada.

É nela que estão localizadas os algoritmos responsáveis por chamar as funções Largura, Profundidade e Dijkstra. 

* Class Grafo

Nessa classe, as funções recebem os dados extraidos na Class Arquivo e calcula a Largura, Profundidade e o menor caminho. 

* Class Main

É a classe responsavel por fazer as validações nos arquivos de entrada e saída e por executar a lista de comandos do arquivo de entrada.

* Class Interface

Responsavel por carregar a interface utilizada no projeto.

# API Rest

Foi implementado uma API Rest utilizando o framework Flask, veja abaixo a documentação:

Para startar a api, navegue até a pasta api pelo prompt de comando e execute o comando:

py api.py

feito isso será iniciado um servidor para as requisições, cujo endereço: 

### Gerar um grafo:

> **Url**: /criaGrafo  
> **Tipo de requisição**: POST  
> **Parâmetros**:   
> - vertices: Ex: 1 2 3 4 5
> - arestas: Ex: [v1, v2, peso], [v3, v4, peso] 
> - digrafo: Ex: true
> - peso: Ex: true

### Calculo de distancia:

> **Url**: /distancia  
> **Tipo de requisição**: GET  
> **Parâmetros**:   
> - Caminho: Ex: 1 2 3 4

### Busca em largura:

> **Url**: /largura  
> **Tipo de requisição**: GET  
> **Parâmetros**:   
> - Origem 
> - Destino

### Busca em profundidade:

> **Url**: /profundidade  
> **Tipo de requisição**: GET  
> **Parâmetros**:   
> - Origem 
> - Destino

### Calculo menor caminho:

> **Url**: /dijkstra  
> **Tipo de requisição**: GET  
> **Parâmetros**:   
> - Origem 
> - Destino

### Árvore geradora minima:

> **Url**: /prim  
> **Tipo de requisição**: GET  
> **Parâmetros**:   
> - Origem 



