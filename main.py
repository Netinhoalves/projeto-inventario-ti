import sqlite3
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Colaborador(BaseModel):
    nome: str
    matricula: str
    setor: str
    modelo_trabalho: str
    email: str

@app.get("/")
def health_check():
    return {"status": "online", "message": "API de Inventário rodando!"}

@app.post("/colaboradores")
def criar_colaborador(colaborador: Colaborador):
    conn = sqlite3.connect('inventario.db')
    cursor = conn.cursor()

    sql = """
    INSERT INTO colaboradores (nome, matricula, setor, modelo_trabalho, email)
    VALUES (?, ?, ?, ?, ?)
    """

    try:
        cursor.execute(sql, (
            colaborador.nome,
            colaborador.matricula,
            colaborador.setor,
            colaborador.modelo_trabalho,
            colaborador.email
        ))
        conn.commit()
        mensagem = "Colaborador cadastrado com sucesso!"
    except sqlite3.IntegrityError:
        mensagem = "Erro: Matrícula ou Email já existem!"
    finally:
        conn.close()

    return {"mensagem": mensagem, "dados_recebidos": colaborador}

@app.get("/colaboradores")
def listar_colaboradores():
    conn = sqlite3.connect('inventario.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM colaboradores")
    resultado = cursor.fetchall()
    
    conn.close()
    
    return resultado