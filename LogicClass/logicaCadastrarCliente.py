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


def cadastrarTxt(nome, cpf, rg, telefone, email, nProcesso):

    directory = "Cadastrados"
    nomeArquivo = cpf
    arquivo = open(directory + "/" + nomeArquivo, "x")
    arquivo.write("Nome: %s\n CPF: %s\n RG: %s\n Telefone: %s\n Emai: %s\n Numero do Processo: %s" %
                  (nome, cpf, rg, telefone, email, nProcesso))


'''
Função de cadastrar os dados no database 

'''


def cadastrarDatabase(nome, cpf, rg, telefone, email, nProcesso):

    # cria uma conexão com o banco de dados
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='cadastroclientes',
    )

    # inicia conexão
    cursor = conexao.cursor()

    # insere os dados no bd usando o create
    # insere os dados na linha do banco de dado
    inserirDb = "INSERT INTO clientes (Nome, CPF, RG, Telefone, Email, nProcesso) VALUES (%s,%s,%s,%s,%s,%s)"
    dados = (nome, cpf, rg, telefone, email, nProcesso)
    cursor.execute(inserirDb, dados)
    conexao.commit()  # edita o banco de dados

    # encerra conexão
    cursor.close()
    conexao.close()
