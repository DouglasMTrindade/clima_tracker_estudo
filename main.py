from localizacao import busca_localizacao
from clima import clima_agora
from log import salva_log
from valida_entrada import menu
import clima_historico

if __name__ == '__main__':
    clima_historico.cria_tabela()
    lista_menu = {
        0 : "MENU",
        1 : "Consultar e salvar clima",
        2 : "Lista histórico completo",
        3 : "Filtrar por cidade",
        4 : "Apagar registro",
        5 : "Sair"
    }
    

    while True:
        opcao = menu(lista_menu)

        if opcao == 1:
            local = busca_localizacao()
            if local:
                clima, agora = clima_agora(local)
                if clima and agora:
                    clima_historico.salva_consulta(local,clima, agora)
                    print(clima, agora)
            else:
                clima, agora = None, None
            
        elif opcao == 2:
            clima_historico.lista_consultas()
        elif opcao == 3:
            clima_historico.filtrar_por_cidade()
        elif opcao == 4:
            clima_historico.apagar_por_id()
        elif opcao == 5:
            break
        else:
            if opcao != 0:
                print(f"Opcao {opcao}, Inválida")
                
    print("Programa Finalizado")