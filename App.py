from asyncio.windows_events import NULL
from LogicClass import logicaCadastrarCliente
from LogicClass import logicaAcessarCliente
from LogicClass import logicaExcluirCliente

'''
Menu de opções
'''
opcao = 0

while opcao != "4":
    print("1 - Cadastrar Novo Cliente\n2- Acessar Cliente Cadastrado\n3- Excluir Cliente Cadastrado\n4 - Sair do Programa\n")
    opcao = input("INFORME A OPCAO: ")

    if opcao == "1":
        nome = str(input("\nInforme o nome do cliente:"))
        cpf = str(input("Informe o cpf do cliente:"))
        rg = str(input("Informe o rg do cliente:"))
        telefone = str(input("Informe o telefone do cliente:"))
        email = str(input("Informe o email do cliente:"))
        nProcesso = str(input("Informe o numero do processo do cliente:"))
        logicaCadastrarCliente.cadastrarTxt(
            nome, rg, cpf, telefone, email, nProcesso)
        print("\n\nCLIENTE CADASTRADO COM SUCESSO\n\n")
    if opcao == "2":
        cpf = str(input("\nInforme o CPF do cliente que será acessado:"))
        logicaAcessarCliente.acessarTxt(cpf)
    if opcao == "3":
        cpf = str(
            input("\nInforme o CPF do cliente que será excluido - 0 PARA SAIR: "))
        logicaExcluirCliente.excluirTxt(cpf)
    elif opcao == "0":
        break
