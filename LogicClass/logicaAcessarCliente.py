"""
Remover Cliente (integrar com banco de dados)
"""
import mysql.connector
'''
Função de acessar o arquivo
com os dados salvos
'''


def acessarTxt(cpf):

    nomeArquivo = cpf
    directory = "Cadastrados"

    arquivo = open(directory + "/" + nomeArquivo, "r")
    for linha in arquivo:
        print(linha)


'''
Função de acessar os dados no database

'''


def acessarDatabase(cpf):

    # cria uma conexão com o banco de dados
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='cadastroclientes',
    )

    # inicia conexão
    cursor = conexao.cursor()

    comando = f'SELECT * FROM clientes WHERE CPF = "{cpf}"'

    cursor.execute(comando)

    dadosAcessados = cursor.fetchall()  # ler o banco de dados

    print(dadosAcessados)
