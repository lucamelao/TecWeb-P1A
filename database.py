import sqlite3
from dataclasses import dataclass

# definição da classe note, importada do python
@dataclass
class Note:
    id: int = None
    title: str = None
    content: str = ''

class Database:
    def __init__(self, db_name):
        # faz a conexão com o banco de dados
        # importante notar a extensão .db no arquivo do banco de dados
        self.conn = sqlite3.connect(db_name + ".db")
        # cria a tabela chamada note
        # colunas id (chave primária int), title (str), content (str não vazia)
        self.conn.execute("CREATE TABLE IF NOT EXISTS note (id INTEGER PRIMARY KEY, title STRING, content STRING NOT NULL);")

    # INSERÇÃO DE DADOS
    def add(self, note: "Note"):
        self.conn.execute(f"INSERT INTO note (title, content) VALUES('{note.title}', '{note.content}');")
        self.conn.commit()

    # CONSULTA DE DADOS
    def get_all(self):
    # não recebe nenhum argumento e devolve uma lista de Note com os valores obtidos do banco de dados
        # declara a lista de notes que será devolvida
        notes_list = []
        # executa o comando e obtém um sqlite3.Cursor
        cursor = self.conn.execute("SELECT id, title, content FROM note")
        # percorre os dados obtidos a partir da consulta e preenche a lista
        for linha in cursor:
            id = linha[0]
            title = linha[1]
            content = linha[2]
            note = Note(id, title, content)
            notes_list.append(note)
        return notes_list

    # ATUALIZAÇÃO DE DADOS
    def update(self, entry: "Note"):
        self.conn.execute(f"UPDATE note SET title = '{entry.title}', content = '{entry.content}' WHERE id = {entry.id};")
        self.conn.commit()

    # DELETAR DADOS 
    # O identificador passa a ter valor inexistente após essa operação
    def delete(self, note_id):
        self.conn.execute(f"DELETE FROM note WHERE id = {note_id};")
        self.conn.commit()