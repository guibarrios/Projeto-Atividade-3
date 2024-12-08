def executar(novaTarefa):
    try:
        with open("dados/tarefas.csv", "a", encoding="utf8") as arquivo:
            novaLinha = "\n" + ",".join([
                novaTarefa["id"],
                novaTarefa["descricao"],
                novaTarefa["prioridade"],
                novaTarefa["dataInicial"],
                novaTarefa["dataFinal"],
                novaTarefa["categoria"],
                novaTarefa["status"],
            ])
            arquivo.write(novaLinha)
        return True
    except Exception as erro:
        print("\n ERRO: ", erro)
        return False