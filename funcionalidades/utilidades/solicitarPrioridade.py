def executar(mensagem, aceitaVazio = False):
    prioridade = ""
    while prioridade not in ["alta", "normal", "baixa"]:
        prioridadeDigitada = input(mensagem)
        
        if aceitaVazio and prioridadeDigitada == "":
            return ""

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