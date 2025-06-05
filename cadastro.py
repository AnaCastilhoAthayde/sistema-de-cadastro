def cadastrar_nome(cadastro):
    novo_nome = input("Digite o nome da Pessoa:" )
    cadastro.append(novo_nome)
    print(f"Usuário {novo_nome} foi adicionado com sucesso")

def lista_nomes(cadastro):
        print("\nLista de nomes cadastrados:")
        for i, nome in enumerate(cadastro,start=1):
            print(f" {i}. {nome}")

def excluir_cadastro(cadastro):         
    excluir_nome = input("Digite o nome para excluir: ")
    if excluir_nome in cadastro:
         cadastro.remove(excluir_nome)
    print(f"{excluir_nome} foi removido.")

def nao_encontrado(cadastro):
      print("Nome não encontrado.")

def sair_do_cadastro(cadastro):
     print("Saindo...")


def menu():
    cadastro = []
    while True:
        print("\n-------------Cadastro de Funcionários---------------------")
        print("[1] Cadastar pessoas")
        print("[2] Listar pessoas")
        print("[3] Excluir Pessoas")
        print("[0]")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_nome(cadastro)
        elif opcao == '2':
            lista_nomes(cadastro)
            
        elif opcao =='3':
            excluir_cadastro(cadastro)
     
        elif opcao == '0':
            sair_do_cadastro
                 
        else:
            print("!!!!! Opção Inválida. Tente Novamente!!!!!")


#Chamda de funcao
menu()
      