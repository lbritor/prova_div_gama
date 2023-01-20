"""
Escreva a função obter_colecao_mongodb(url_conexao, colecao) que irá se conectar no MogodDB utilizando alguma
biblioteca do Python. Ela possui os seguintes parâmetros:

○ url_conexao: URI de conexão com banco de dados MongoDB, que também informa a base de dados (database).
Por exemplo: a URI `mongodb://localhost/bancoexemplo', é a string de conexão para o banco "bancoexemplo"
da minha máquina local ("localhost").

○ colecao: É o nome da coleção (collection) do MongoDB que estaremos acessando com esta função.
"""

from pymongo import MongoClient

def obter_colecao_mongodb(url_conexao: str, colecao):
    client = MongoClient(url_conexao)
    colecao = client[colecao]
    return colecao
