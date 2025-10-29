from clima.localizacao import busca_localizacao
from clima.clima import clima_agora
from utils.log import salva_log
from clima.valida_entrada import menu
from database import conexao

if __name__ == '__main__':
    conexao.cria_tabela()
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
                    conexao.salva_consulta(local,clima, agora)
                    print(clima, agora)
            else:
                clima, agora = None, None
            
        elif opcao == 2:
            conexao.lista_consultas()
        elif opcao == 3:
            conexao.filtrar_por_cidade()
        elif opcao == 4:
            conexao.apagar_por_id()
        elif opcao == 5:
            break
        else:
            if opcao != 0:
                print(f"Opcao {opcao}, Inválida")
                
    print("Programa Finalizado")