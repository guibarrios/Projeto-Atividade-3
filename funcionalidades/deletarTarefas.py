from servicos import atualizarDados, obterTarefas

def executar(idEncontrado):
    tarefas = obterTarefas.executar()
    tarefaEncontrada = None

    for tarefa in tarefas:
        if tarefa.get("id") == idEncontrado:
            tarefaEncontrada = tarefa

    if tarefaEncontrada is None:
        print(f"Nenhuma tarefa encontrada com o ID {idEncontrado}")
        return
    
    print("\n ** Tarefa encontrada **")   
    for chave, valor in tarefaEncontrada.items():
        print(f"{chave}: {"(vazio)" if len(valor) ==0 else valor }")

    escolha = input("\n Confirma exclusão? (s/n): ")
    
    if escolha != "s":
        print("\n ** Exclusão cancelada **")
        return
    
    tarefasFiltradas = []
    for tarefa in tarefas:
        if tarefa.get("id") != idEncontrado:
            tarefasFiltradas.append(tarefa)


    validarExclusao = atualizarDados.executar(tarefasFiltradas)

    if validarExclusao:
        print("Foi deletado a tarefa")
        # print(f"Foi deletado a tarefa {idTarefa} {nomeTarefa.get("descricao")}")
    else:
        print("A tarefa não foi deletada") 