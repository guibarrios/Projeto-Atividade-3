def executar (novasTarefas):
    linhas = []
    for tarefa in novasTarefas:
        linha = "\n" + ",".join([
            tarefa["id"],
            tarefa["descricao"],
            tarefa["prioridade"],
            tarefa["dataInicial"],
            tarefa["dataFinal"],
            tarefa["categoria"],
            tarefa["status"],
        ])
        linhas.append(linha)

    primeiraLinha = "id,descricao,prioridade,dataInicial,dataFinal,categoria,status"
    linhas.insert(0, primeiraLinha)

    try:
        with open("dados/tarefas.csv", "w", encoding="utf8") as arquivo:
            arquivo.writelines(linhas)
        return True
    except Exception as erro:
        print("Ocorreu erro ao tentar atualizar os dados", erro)
        return False