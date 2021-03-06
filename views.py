from utils import load_data, load_template, add_note, delete_note, edit_note, build_response
from urllib import parse

def index(request):    
    # Cria uma lista de <li>'s para cada anotação
    note_template = load_template('components/note.html')
    notes_li = [
        note_template.format(title = dados.title, details = dados.content, id = dados.id)
        for dados in load_data()
    ]
    notes = '\n'.join(notes_li)
    
    # A string de request sempre começa com o tipo da requisição (ex: GET, POST)
    if request.startswith('POST'):
        request = request.replace('\r', '')  # Remove caracteres indesejados
        # Cabeçalho e corpo estão sempre separados por duas quebras de linha
        partes = request.split('\n\n')
        # print(partes)
        corpo = partes[1]
        params = {}
        # Preencha o dicionário params com as informações do corpo da requisição
        # O dicionário conterá dois valores, o título e a descrição.
        # Posteriormente pode ser interessante criar uma função que recebe a
        # requisição e devolve os parâmetros para desacoplar esta lógica.
        # Dica: use o método split da string e a função unquote_plus
        for chave_valor in corpo.split('&'):
            chave, valor = chave_valor.split('=')
            params[parse.unquote_plus(chave)] = parse.unquote_plus(valor)
        add_note(params)
        return build_response(body=load_template('index.html').format(notes=notes), code=303, reason='See Other', headers='Location: /')    
    return build_response(body=load_template('index.html').format(notes=notes))

def remove_note(request):
    '''
    Função semelhante à index, mas chama o delete_note de Database para deletar notas.
    '''
    note_template = load_template('components/note.html')
    notes_li = [
        note_template.format(title = dados.title, details = dados.content, id = dados.id)
        for dados in load_data()
    ]
    notes = '\n'.join(notes_li)
    if request.startswith('POST'):
        request = request.replace('\r', '')  
        partes = request.split('\n\n')
        # print(partes)
        corpo = partes[1]
        params = {}
        for chave_valor in corpo.split('&'):
            chave, valor = chave_valor.split('=')
            params[parse.unquote_plus(chave)] = parse.unquote_plus(valor)
        # deleta a nota com o id específico (remove do Database)
        delete_note(params['id'])
        return build_response(body=load_template('index.html').format(notes=notes), code=303, reason='See Other', headers='Location: /')    
    return build_response(body=load_template('index.html').format(notes=notes))

def update_note(request):
    '''
    Função semelhante à index e remove_note, mas chama o edit_note de Database para atualizar notas no db.
    '''
    note_template = load_template('components/note.html')
    notes_li = [
        note_template.format(title = dados.title, details = dados.content, id = dados.id)
        for dados in load_data()
    ]
    notes = '\n'.join(notes_li)
    if request.startswith('POST'):
        request = request.replace('\r', '')  
        partes = request.split('\n\n')
        # print(partes)
        corpo = partes[1]
        params = {}
        for chave_valor in corpo.split('&'):
            chave, valor = chave_valor.split('=')
            params[parse.unquote_plus(chave)] = parse.unquote_plus(valor)
        # atualiza a nota com o id específico 
        edit_note(params)
        return build_response(body=load_template('index.html').format(notes=notes), code=303, reason='See Other', headers='Location: /')    
    return build_response(body=load_template('index.html').format(notes=notes))
