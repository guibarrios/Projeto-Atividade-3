def executar():
    tarefas = []
    try:
        with open("dados/tarefas.csv", "r", encoding="utf8") as arquivo:
            linha_atual = 0
            for linha in arquivo:
                if linha_atual == 0:
                    linha_atual += 1
                else:
                    valores = linha.split(",")
                    tarefa = {
                        "id": valores[0].strip(),
                        "descricao": valores[1].strip(),
                        "prioridade": valores[2].strip(),
                        "dataInicial": valores[3].strip(),
                        "dataFinal": valores[4].strip(),
                        "categoria": valores[5].strip(),
                        "status": valores[6].strip(),
                    }
                    tarefas.append(tarefa)
    except FileNotFoundError:
        print("Arquivo 'tarefas.csv' não encontrado")

    return tarefas