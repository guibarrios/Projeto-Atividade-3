menuOpcoes = [
    "1 - Criar contas",
    "2 - Listar conta",
    "3 - Atualizar conta",
    "4 - Excluir conta",
    "5 - Sair",
]

def menuPrincipal ():
    while True:
        print("\nMenu principal\n")
        for listaOpcoes in menuOpcoes:
            print(listaOpcoes)
        opcaoEscolhida = input("\nEscolha uma opção: ")
        match opcaoEscolhida:
              case "1":
                    print("\nCriar contas")
              case "2":
                    print("\nListar conta")
              case "3":
                    print("\nAtualizar conta")
              case "4":
                    print("\nExcluir conta")
              case "5":
                    print("\nEncerrado")
                    break
              case _:
                    print("\nOpção inválida")


menuPrincipal()