from funcionalidades import listarTarefasPorTipo

opcaoPrioridade = {
    "1": "alta",
    "2": "normal",
    "3": "baixa",
    "4": "todas",
}

def executar():
    tipo = obterPrioridade()
    listarTarefasPorTipo.executar(tipo=tipo)

def obterPrioridade():
    escolha = ""
    while escolha not in opcaoPrioridade:
        print("1 - Tarefas com prioridade alta")
        print("2 - Tarefas com prioridade normal")
        print("3 - Tarefas com prioridade baixa")
        print("4 - Todas tarefas")
        escolha = input("Escolha uma opção: ")
        if escolha in opcaoPrioridade:
            return opcaoPrioridade[escolha]
        print("\nOpção incorreta")