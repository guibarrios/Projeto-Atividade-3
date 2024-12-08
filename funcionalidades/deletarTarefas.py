from servicos import obterTarefas, atualizarTarefas

def executar(idTarefa):
    tarefas = obterTarefas.executar()
    idEncontrado = None

    for tarefa in tarefas:
        if tarefa.get("id") == idTarefa:
            idEncontrado = tarefa

    if idEncontrado is None:
        print(f"Nenhuma tarefa encontrada com o ID {idTarefa}")
        return
    
    print("\ ** Conta encontrada **")   
    for chave, valor in idEncontrado.items():
        print(f"{chave}: {"(vazio)" if len(valor) ==0 else valor }")

    escolha = input("\n Confirma exclusão? (s/n): ")
    
    if escolha != "s":
        print("Exclusão cancelada")
        return
    
    tarefasFiltradas = []
    for tarefa in tarefas:
        if tarefa.get("id") != idTarefa:
            tarefasFiltradas.append(tarefa)


    validarExclusao = atualizarTarefas.executar(tarefasFiltradas)

    if validarExclusao:
        print("Foi deletado a tarefa")
        # print(f"Foi deletado a tarefa {idTarefa} {nomeTarefa.get("descricao")}")
    else:
        print("A tarefa não foi deletada") 