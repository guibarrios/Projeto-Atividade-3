from servicos import atualizarDados, obterTarefas
from funcionalidades.utilidades import solicitarStatus, solicitarPrioridade

def executar(idEncontrado):
    tarefas = obterTarefas.executar()
    tarefaEncontrada = None

    for posicao, conta in enumerate(tarefas):
        if conta.get("id") == idEncontrado:
            tarefaEncontrada = posicao
            break
    
    if tarefaEncontrada is None:
        print(f"Nenhuma tarefa encontrada com o ID {idEncontrado}")
        return
    
    print("\n ** Tarefa encontrada **")
    print("** Presiona 'ENTER' para manter o valor atual **\n")
    for chave, valor in tarefas[tarefaEncontrada].items():
        if chave == "id":
            continue

        novoValor = ""
        mensagem = f"{chave} atual: {valor}\n"

        if chave == "prioridade":
            novoValor = solicitarPrioridade.executar(f"{mensagem}1 = alta \n2 = normal \n3 = baixa \nDigite uma opção ou pressione 'ENTER' para não alterar: ", aceitaVazio=True)
        elif chave == "status":
            novoValor = solicitarStatus.executar(f"{mensagem}1 = concluido \n2 = em andamento \n3 = pendente \nDigite uma opção ou pressione 'ENTER' para não alterar: ", aceitaVazio=True)
        else:
            novoValor = input(f"{mensagem}Digite novo valor: ")

        tarefas[tarefaEncontrada][chave] = novoValor if len(novoValor) > 0 else valor

    tarefaAtualizada = atualizarDados.executar(tarefas)

    if tarefaAtualizada:
        print("\nTarefa atualizada com sucesso")
        return
    print("\nNão foi possivel atualizar a tarefa")