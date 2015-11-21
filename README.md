Trabalho de Teoria da Computação
=================================================

Grafos
------

Projeto apresentado à disciplina de Teoria da Computação do curso de Ciência da Computação Pitágoras Betim.

Orientador: [Fernando Braz](https://github.com/fernandoafb)

##Integrantes deste projeto:

*[Robson Alves](https://github.com/robsonalvesbh)
*Marcela Fernandes
*Isaac Oliveira
*Junio Almeida
*Dhéssika Gomes

##Linguagem Utilizada

*Python 3.5.0

Neste projeto foi implementado os seguintes algoritmos:

*Calculo de distancia

*Busca em Largura

Com esse algoritmo é possivel fazer busca em um grafo partindo de um vértice origem, ele percorre seus vizinhos até encontrar o vértice 
desejado. Ele pode ser usado para verificar a conectividade entre os vétices do grafo e também para verificar se um grafo é biparte.

*Busca em Profundidade

Com esse algoritmo é possivel fazer busca em um grafo partindo de um vértice origem, percorrendo todos os vertices de seu ramo, até encontrar
o vertice desejado. Ele é usado para solucionar problemas como o de labirinto e de quebra cabeça. 

*Dijkstra

É um algoritmo usado para identificar qual o menor caminho dentro de um grafo. Ele é utilizado por exemplo para definir 
qual o menor caminho entre duas cidades, como Belo Horizonte e São Paulo.

*Prim

*Kruskal


##Bibliotecas e pacotes utilizadas

*Pacote Numpy
*Biblioteca Networkx
*Biblioteca Matplotlib
*Pacote Tkinter (Interface gráfica)

Instale todas as bibliotecas automaticamente utilizando arquivo requirements através do gerenciador de dependencia do Python, o PIP.
Para instalar, Execute o comando pip install -r requirements.txt

##Classes Utilizadas

*Class Arquivo

Dentro dessa classe, encontra-se as funções responsaveis por abrir, ler e gravar em cada variavel os dados contidos no arquivo de entrada.

É nela que estão localizadas os algoritmos responsáveis por chamar as funções Largura, Profundidade e Dijkstra. 

*Class Grafo

Nessa classe, as funções recebem os dados extraidos na Class Arquivo e calcula a Largura, Profundidade e o menor caminho. 

*Class Main

É a classe responsavel por fazer as validações nos arquivos de entrada e saída e por executar a lista de comandos do arquivo de entrada.

*Class Erro

Responsavel por avisar ao usuario se o arquivo de entrada está vazio e se o arquivo não foi selecionado.

*Class Interface

Responsavel por carregar a interface utilizada no projeto.










m