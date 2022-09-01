"""
Acessar Cliente (mostra os dados dos clientes/integrar com banco de dado)
    MOSTRAR TODOS OS DADOS CADASTRADOS DO CLIENTE
"""
import os
import mysql.connector

'''
Função de excluir o arquivo 
com os dados salvos
'''


def excluirTxt(cpf):
    nomeArquivo = cpf
    directory = "Cadastrados"
    os.remove(directory + "/" + nomeArquivo,)


'''
Função de excluir os dados no database 

'''


def excluirDatabase(cpf):
    # cria uma conexão com o banco de dados
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='cadastroclientes',
    )

    # inicia conexão
    cursor = conexao.cursor()

    # exclui os dados no bd usando o create
    excluirDb = f'DELETE FROM clientes WHERE CPF = "{cpf}"'
    cursor.execute(excluirDb)
    conexao.commit()  # edita o banco de dados

    # encerra conexão
    cursor.close()
    conexao.close()