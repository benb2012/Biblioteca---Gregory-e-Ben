import sqlite3


def verificar_id_existente(tabela, id):
    conn = sqlite3.connect("biblioteca.db")
    cursor = conn.cursor()

    # Montando a consulta SQL para verificar se o ID existe na tabela especificada
    consulta = f"SELECT COUNT(*) FROM {tabela} WHERE id = ?"
    cursor.execute(consulta, (id,))
    resultado = cursor.fetchone()

    conn.close()

    # Retorna True se o ID existir, caso contrário, retorna False
    return resultado is not None