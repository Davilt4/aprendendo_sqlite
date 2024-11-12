import sqlite3
from pathlib import Path

pessoas_db = Path(__file__).parent / 'pessoas.db'

def criar_tabela(conn):
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pessoas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            idade INTEGER NOT NULL
        )
    """)
    conn.commit()
    cursor.close()

def conectar():
    conn = sqlite3.connect(pessoas_db)
    return conn

def cadastrar_pessoa(conn, pessoa):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO pessoas (nome, idade) VALUES (?, ?)", (pessoa.nome, pessoa.idade))
    conn.commit()
    cursor.close()

def deletar_pessoa(conn, pessoa_id):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM pessoas WHERE id = ?", (pessoa_id,))
    conn.commit()
    cursor.close()

def listar_pessoas(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM pessoas")
    pessoas = cursor.fetchall()
    cursor.close()
    return pessoas