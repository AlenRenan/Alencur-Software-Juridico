"""
Remover Cliente (integrar com banco de dados)
"""

'''
Função de acessar o arquivo 
com os dados salvos
'''
import mysql.connector

def acessarTxt(cpf):

    nomeArquivo = cpf
    directory = "Cadastrados"

    arquivo = open(directory + "/" + nomeArquivo, "r")
    for linha in arquivo:
        print(linha)


'''
Função de acessar os dados no database 

'''


def acessarDatabase():
    print()
