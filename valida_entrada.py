

def le_int(mensagem):
    """
    Lê um número inteiro do usuário com tratamento de erro.

    Args:
        msg (str): Mensagem exibida ao usuário.

    Returns:
        int: Valor inteiro digitado.
    """
    valido = True
    while valido:
        try:
            valor = int(input(mensagem).strip())
            valido = False
        except ValueError:
            print("Valor digitado invalido, Digite novamente")
    
    return valor


def menu (lista_menu):
    """
    Exibe um menu dinâmico baseado em uma lista de opções.

    Args:
        opcoes (list): lista de opções (strings)

    Returns:
        int: opção escolhida pelo usuário
    """
    print("MENU")
    for chave,valor in lista_menu.items():
        print(f"[{chave}] - {valor}")

    while True:
        opcao = le_int("Escolha uma opção: ")

        if opcao in lista_menu:
            return opcao
        else:
            print("Opção Inválida! Tente novamente")
            