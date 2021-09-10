import json
import sqlite3
from database import Database, Note

def extract_route(requisicao):
    if requisicao.startswith('GET'):
        lista1 = requisicao.split("GET /")
    else:
        lista1 = requisicao.split("POST /")

    lista2 = lista1[1].split(" ")
    return lista2[0]

def read_file(path):
    lista = str(path)
    if lista[-1] == 'txt' or lista[-1] == 'css' or lista[-1] == 'js' or lista[-1] == 'html':
        return(open(path))
    else:
        return(open(path, 'rb').read())

def load_data():
    # cria o objeto db para chamada de funções
    db = Database('Get-it Notes')
    # método de Database que consulta dados
    return db.get_all()

def load_template(filename):
    return(open('templates/'+filename).read())

def add_note(new_note):
    # cria o objeto db para chamada de funções
    db = Database('Get-it Notes')
    # adiciona uma nota nova
    db.add(Note(title = new_note['titulo'], content = new_note['detalhes']))

def delete_note(id):
    # cria o objeto db para chamada de funções
    db = Database('Get-it Notes')
    # deleta a nota com o id indicado
    db.delete(id)

def edit_note(modified_note):
    # cria o objeto db para chamada de funções
    db = Database('Get-it Notes')
    # atualiza a note
    id = modified_note['id']
    titulo = modified_note['title']
    conteudo = modified_note['content']
    db.update(Note(id = id, title = titulo, content = conteudo))

def build_response(body='', code=200, reason='OK', headers=''):
    if headers=='':
        return ('HTTP/1.1 '+str(code)+' '+reason+'\n\n'+body).encode()
    return ('HTTP/1.1 '+str(code)+' '+reason+'\n'+headers+'\n\n'+body).encode()