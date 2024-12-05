from servicos import (
    obterProximoId,
    salvarConta,
)
from funcionalidades.utilidades import (
    validarData,
    solicitarPrioridade,
    solicitarStatus,
)

def executar():

    print("Informe os dados da tarefa: ")
    descricao = input("Qual é a descrição? ")
    prioridade = solicitarPrioridade.executar("Qual a prioridade? '1 - alta', '2 - normal', '3 - baixa': ")
    dataInicial = validarData.executar(input("Qual é a data inicial? (DD/MM/YYY): "))
    dataFinal = validarData.executar(input("Qual é a data final? (DD/MM/YYY): "))
    categoria = input("Qual é a categoria? ")
    status = solicitarStatus.executar("Qual o status? '1 - concluido', '2 - em andamento', '3 - pendente': ")

    novaTarefa = {
        "id": obterProximoId.executar(),
        "descricao": descricao,
        "prioridade": prioridade,
        "dataInicial": dataInicial,
        "dataFinal": dataFinal,
        "categoria": categoria,
        "status": status,
    }

    validarSalvamento = salvarConta.executar(novaTarefa)

    if validarSalvamento:
        print("Tarefa salva com sucesso")
    else:
        print("Não foi possível salvar a tarefa")