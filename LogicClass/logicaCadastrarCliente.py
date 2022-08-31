"""
Cadastrar Cliente (integrar com banco de dados)
     NOME COMPLETO
     CPF
     RG
     TELEFONE
     EMAIL
     NUMERO DO PROCESSO
"""
import mysql.connector


def cadastrarTxt(nome, rg, cpf, telefone, email, nProcesso):

    directory = "Cadastrados"
    nomeArquivo = cpf
    arquivo = open(directory + "/" + nomeArquivo, "x")
    arquivo.write("Nome: %s\n RG: %s\n CPF: %s\n Telefone: %s\n Emai: %s\n Numero do Processo: %s" %
                  (nome, rg, cpf, telefone, email, nProcesso))


'''
Função de cadastrar os dados no database 

'''


def cadastrarDatabase():
    print()
