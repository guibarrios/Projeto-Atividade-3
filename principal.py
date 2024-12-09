from datetime import datetime
from os import system
from controles import (
    listarTarefas,
    criarTarefas,
    excluirTarefa,
    atualizarTarefa

)

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
                  criarTarefas.executar()
              case "2":
                  listarTarefas.executar()
              case "3":
                  atualizarTarefa.executar()
              case "4":
                  excluirTarefa.executar()
              case "5":
                  print("\nEncerrado")
                  print(menuOpcoes[4])
                  break
              case _:
                    print("\nOpção inválida")


if __name__ == "__main__":
    system('clear')
    print(datetime.now().strftime("%d/%m/%Y, %H:%M"))
    menuPrincipal()
