from datetime import datetime
from controles import listarTarefas

menuOpcoes = [
    "1 - Criar tarefa",
    "2 - Listar tarefas",
    "3 - Atualizar tarefa",
    "4 - Excluir tarefa",
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
                  print(menuOpcoes[0])
              case "2":
                  listarTarefas.executar()
              case "3":
                  print(menuOpcoes[2])
              case "4":
                  print(menuOpcoes[3])
              case "5":
                  print("\nEncerrado")
                  print(menuOpcoes[4])
                  break
              case _:
                    print("\nOpção inválida")


if __name__ == "__main__":
    print(datetime.now().strftime("%d/%m/%Y, %H:%M"))
    menuPrincipal()