from funcionalidades import atualizarTarefas

def executar ():
    idTarefa = input("Informe o ID da tarefa: ")

    if not(idTarefa.isnumeric()):
        print("O ID informado é inválido")
        return
    
    atualizarTarefas.executar(idEncontrado=idTarefa)