from database import Database
from database import Note

db = Database('banco')

# testa a funcionalidade de adição de dados ao banco
# db.add(Note(title='Pão doce', content='Abra o pão e coloque o seu suco em pó favorito.'))
# db.add(Note(title=None, content='Lembrar de tomar água'))

# testa a funcionalidade de consulta ao banco de dados
notes = db.get_all()
for note in notes:
    print(f'Anotação {note.id}:\n  Título: {note.title}\n  Conteúdo: {note.content}\n')

# testa a funcionalidade do update ao banco de dados
# db.update(Note(title='Agora tenho título', content='Não esquecer da água!', id = 2))