import sqlite3

conn = sqlite3.connect('inventario.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS colaboradores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    matricula TEXT UNIQUE NOT NULL,
    setor TEXT NOT NULL,
    modelo_trabalho TEXT,
    email TEXT UNIQUE NOT NULL
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS ativos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tipo TEXT NOT NULL,
    modelo TEXT NOT NULL,
    s_n TEXT UNIQUE NOT NULL,
    hostname TEXT,
    ip TEXT,
    status TEXT NOT NULL
);
""")

conn.commit()
conn.close()

print("Banco de dados 'inventario.db' inicializado com sucesso.")