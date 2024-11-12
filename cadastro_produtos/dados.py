import sqlite3
from pathlib import Path

dataBase_path = Path(__file__).parent / 'produtos.db'

def conectar():
    conn = sqlite3.connect(dataBase_path)
    return conn

def criar_tabela(conn):
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            preco REAL NOT NULL,
            validade TEXT NOT NULL,
            fabricante TEXT NOT NULL,
            descricao TEXT NOT NULL
        )
    """)
    conn.commit()
    cursor.close()

def cadastrar_produto(conn, produto):
    cursor = conn.cursor()    
    cursor.execute("INSERT INTO produtos (nome, preco, validade, fabricante, descricao) VALUES (?, ?, ?, ?, ?)", (produto.nome, produto.preco, produto.validade, produto.fabricante, produto.descricao))
    conn.commit()
    cursor.close()

def listar_produtos(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()
    cursor.close()
    return produtos

def deletar_produto(conn, produto_id):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM produtos WHERE id = ?", (produto_id,))
    conn.commit()
    cursor.close()