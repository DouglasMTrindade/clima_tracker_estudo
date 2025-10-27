import sqlite3
from valida_entrada import le_int


def cria_tabela():
    """
    Cria a tabela 'consultas' no banco SQLite, caso ainda não exista.

    Estrutura da tabela:
        - id: inteiro autoincrementado (chave primária)
        - cidade: texto
        - temperatura: texto
        - descricao: texto
        - data_hora: texto
    Returns:
        None
    """
    with sqlite3.connect('consultas.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS consultas (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   cidade TEXT,
                   temperatura TEXT,
                   descricao TEXT,
                   data_hora TEXT
                   )
        ''')
        conn.commit()
    


def salva_consulta (local,clima,agora):
    """
    Insere uma nova consulta de clima no banco de dados.

    Args:
        local (dict): Dados da localização
        clima (dict): Dados do clima
        agora (str): Data e hora formatadas da consulta

    Returns:
        None
    """

    sql = "INSERT INTO consultas(cidade, temperatura, descricao, data_hora) VALUES (?,?,?,?)"
    dados =(
        local['cidade'],
        clima['temperatura'],
        clima['descricao'],
        agora
    )

    try:
        with sqlite3.connect('consultas.db') as conn:
            cursor = conn.cursor()
            cursor.execute (sql, dados)
            conn.commit()
    except sqlite3.Error as e:
        print(f"Erro no banco: {e}")


def lista_consultas():
    """
    Lista todas as consultas salvas no banco de dados.

    Exibe:
        ID | Cidade | Temperatura | Descrição | Data e Hora

    Returns:
        None
    """
    try:
        with sqlite3.connect('consultas.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM consultas")
            rows = cursor.fetchall()

            if rows:
                print("Historico de Consultas")
                for row in rows:
                    print(f"ID {row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]}")
            else:
                print("Nenhum historico encontrado")
    except sqlite3.Error as e:
        print(f"Erro no banco: {e}")


def filtrar_por_cidade():
    """
    Filtra as consultas armazenadas no banco com base no nome da cidade informada pelo usuário.

    Returns:
        None
    """
    cidade = input("Digite a cidade que quer filtrar : ")

    try:
        with sqlite3.connect('consultas.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM consultas WHERE cidade = ?" , (cidade,))
            rows = cursor.fetchall()

            if rows:
                for row in rows:
                    print(f"ID {row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]}")
            else:
                print(f"cidade '{cidade}' nao encontrada no registro")
    except sqlite3.Error as e:
        print(f"Erro no banco {e}")


def apagar_por_id ():
    """
    Apaga um registro específico do banco de dados com base no ID informado pelo usuário.

    Returns:
        None
    """
    lista_consultas()
    id = le_int("informe o ID a ser excluido: ")
    sql = "DELETE FROM consultas WHERE id = ?" 

    try: 
        with sqlite3.connect("consultas.db") as conn:
            cursor = conn.cursor()
            cursor.execute(sql,(id,))
            conn.commit()
            
            if cursor.rowcount > 0:
                print("Registro apagado com sucesso!")
            else:
                print("Nenhum registro encontrado com esse ID")
    except sqlite3.Error as e:
        print("Erro no banco: ", e)
    

