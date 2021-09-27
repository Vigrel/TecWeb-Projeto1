from django.shortcuts import render, redirect
from .models import Note

def index(request):
    if request.method == 'POST':
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        note = Note(title = title, content = content)
        note.save()
        return redirect('index');
    
    else:
        all_notes = Note.objects.all()
        return render(request, 'notes/index.html', {'notes': all_notes})

def delete(req):
    id = req.POST.get('delete')
    note = Note.objects.get(id=int(id))
    note.delete()
    return redirect('index');


def put(req):
    note_req = req.GET.get('put')
    dict = {}

    for i in note_req.split('&'):
        k = i.split('=')[0]
        v = i.split('=')[1]
        dict[k] = v

    note = Note.objects.get(id=int(dict["id"]))
    note.title = dict["title"]
    note.content = dict["content"]
    note.save()

    return redirect('index')