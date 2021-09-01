import json 

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

def load_data(filename):
    return(json.loads(open('data/'+filename, 'rt').read()))

def load_template(filename):
    return(open('templates/'+filename).read())

def add_note(new_note):
    notes = load_data('notes.json')
    notes.append(new_note)
    with open('data/notes.json', 'w') as new:
        json.dump(notes, new)

def build_response(body='', code=200, reason='OK', headers=''):
    if headers=='':
        return ('HTTP/1.1 '+str(code)+' '+reason+'\n\n'+body).encode()
    return ('HTTP/1.1 '+str(code)+' '+reason+'\n'+headers+'\n\n'+body).encode()