def executar(mensagem, aceitaVazio = False):
    status = ""
    while status not in ["concluido", "em andamento", "pendente"]:
        prioridadeDigitada = input(mensagem)

        if aceitaVazio and prioridadeDigitada == "":
            return ""

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