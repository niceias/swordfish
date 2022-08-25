from senhas import Senhas
import senhas

def acesso():
    senha = input('Digite a senha de acesso: ')
    if (senha != 'xpto'):
        for i in range(2):
            senha = input('Digite a senha correta: ')
            if (senha != 'xpto'):
                continue
            else:
                menu()
        print('O programa será encerrado por varias tentivas erradas!!')
    else:
        menu()

def menu():
    print("Cadastrar conta: digite 1")
    print('Pesquisar Contas digite 2')
    print("###############################")
    escolha = input("Digite a escolha: ")
    print("###############################")
    if(escolha == '1'):
        cadastro()
    elif(escolha == '2'):
        try:
            conta.imprime()
            menu()
        except:
            print("Não há registros de contas!!")
            menu()

def cadastro():

    dom = input("Digite o nome da conta: ")
    sen = input("Digite a senha da conta: ")
    global conta
    conta = Senhas(dom, sen)
    menu()


acesso()




