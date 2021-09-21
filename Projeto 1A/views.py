from utils import load_template
from urllib.parse import unquote_plus
from database.database import Database, Note

def index(req):
    db = Database('data/GetItProjectDB')

    if req.startswith('POST'):

        req = req.replace('\r', '')  
        
        partes = req.split('\n\n')
        corpo = partes[1]

        if "delete" in req: db.delete(int(corpo.split("=")[-1]))
        
        else:
            params = {}
            for chave_valor in corpo.split('&'):
                type = unquote_plus(chave_valor.split('=')[0])
                txt = unquote_plus(chave_valor.split('=')[1])
                params[type] = txt
            db.add(Note(title=params["titulo"],content=params["detalhes"]))

    note_template = load_template('components/note.html')
    notes_li = [
        note_template.format(id=dados.id, title=dados.title, details=dados.content)
        for dados in db.get_all()
    ]
    notes = '\n'.join(notes_li)

    return load_template('index.html').format(notes=notes).encode()