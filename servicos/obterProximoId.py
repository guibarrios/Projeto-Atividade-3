from servicos import obterTarefas

def executar():
    verificarId = obterTarefas.executar()
    if len(verificarId) == 0:
        return "1"
    ultimoId = verificarId[-1]
    proximoId = int(ultimoId.get("id", 0)) + 1
    return str(proximoId)