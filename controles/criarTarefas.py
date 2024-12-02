from datetime import datetime

def executar():

    print("Informe os dados: ")
    descricao = input("Qual é a descrição? ")
    prioridade = solicitarPrioridade("Qual a prioridade? '1 - alta', '2 - normal', '3 - baixa': ")
    dataInicial = validarData(input("Qual é a data inicial? (DD/MM/YYY): "))
    dataFinal = validarData(input("Qual é a data final? (DD/MM/YYY): "))
    categoria = input("Qual é a categoria? ")
    status = solicitarstatus("Qual o status? '1 - concluido', '2 - em andamento', '3 - pendente': ")

    novaTarefa = {
        "id": "",
        "descricao": descricao,
        "prioridade": prioridade,
        "dataInicial": dataInicial,
        "dataFinal": dataFinal,
        "categoria": categoria,
        "status": status,
    }

    print(novaTarefa)

def validarData(data):
    if len(data) == 0:
        return datetime.today().strftime("%d/%m/%Y")
    return data

def solicitarPrioridade(mensagem):
    prioridade = ""
    while prioridade not in ["alta", "normal", "baixa"]:
        prioridadeDigitada = input(mensagem)
        match prioridadeDigitada:
            case "1":
                prioridade = "alta"
            case "2":
                prioridade = "normal"
            case "3":
                prioridade = "baixa"
            case _:
                print("\nOpção inválida")
    return prioridade

def solicitarstatus(mensagem):
    status = ""
    while status not in ["concluido", "em andamento", "pendente"]:
        prioridadeDigitada = input(mensagem)
        match prioridadeDigitada:
            case "1":
                status = "concluido"
            case "2":
                status = "em andamento"
            case "3":
                status = "pendente"
            case _:
                print("\nOpção inválida")
    return status