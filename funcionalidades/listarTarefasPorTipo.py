from servicos import obterTarefas
def executar(tipo):
    tarefas = obterTarefas.executar()

    if tipo != "todas":
        tarefas = [tarefa for tarefa in tarefas if tarefa.get("prioridade", "") == tipo]

    for tarefa in tarefas:
        print("\n ---------- // ----------")
        for chave, valor in tarefa.items():
            print(f"{chave}: {"(vazio)" if len(valor) ==0 else valor }")