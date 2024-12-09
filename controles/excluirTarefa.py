from funcionalidades import deletarTarefas

def executar ():
    idTarefa = input("Informe o ID da tarefa: ")

    if not(idTarefa.isnumeric()):
        print("O ID informado é inválido")
        return
    
    deletarTarefas.executar(idEncontrado=idTarefa)