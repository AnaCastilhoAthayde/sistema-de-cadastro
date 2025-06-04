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
            novo_nome = input("Digite o nome da Pessoa:" )
            cadastro.append(novo_nome)
            print(f"Usuário {novo_nome} foi adicionado com sucesso")
        elif opcao == '2':
            print("\nLista de nomes cadastrados:")
            for i, nome in enumerate(cadastro, start=1):
                print(f" {i}. {nome}")
        elif opcao =='3':
            excluir_nome = input("Digite o nome para excluir: ")
            if excluir_nome in cadastro:
                  cadastro.remove(excluir_nome)
                  print(f"{excluir_nome} foi removido.")
            else:
                print("Nome não encontrado.")
        elif opcao == '0':
            print("Sainda...")
            break
        else:
            print("!!!!! OPÇÃO INVÁLIDA.TENTE NOVAMNETE. !!!!!")

#Chamada de funcao
menu()
      