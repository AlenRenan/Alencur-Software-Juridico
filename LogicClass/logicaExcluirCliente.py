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


def excluirDatabase():
    print()
