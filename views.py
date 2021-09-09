from os import error, replace
from utils import load_data, load_template, add_note
from utils import extract_route, read_file, build_response
import urllib

def index(request):

    if request.startswith('POST'):
        request = request.replace('\r', '')  
        partes = request.split('\n\n')
        corpo = partes[0]
        params = {"titulo": '', "detalhes":''}

        for chave_valor in corpo.split('&'):
            if chave_valor.startswith("titulo"):
                params["titulo"] = urllib.parse.unquote_plus(chave_valor[chave_valor.find("=")+1:], encoding="utf-8", errors="replace")
            if chave_valor.startswith("detalhes"):
                params["detalhes"] = urllib.parse.unquote_plus(chave_valor[chave_valor.find("=")+1:], encoding="utf-8", errors="replace")
    
        print(params)
        add_note(params)

    note_template = load_template('components/note.html')
    notes_li = [
        note_template.format(title=dados['titulo'], details=dados['detalhes'])
        for dados in load_data('notes.json')
    ]
    notes = '\n'.join(notes_li)

    return load_template('index.html').format(notes=notes).encode()