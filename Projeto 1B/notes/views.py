from django.shortcuts import render, redirect
from .models import Note, Tag

def index(request):
    if request.method == 'POST':
        title = request.POST.get('titulo');
        content = request.POST.get('detalhes');
        tag_name = request.POST.get('tag');

        if tag_name == '':    
            note = Note(title = title, content = content);
            note.save();
            return redirect('index');

        if Tag.objects.filter(tag=tag_name).exists():
            tag = Tag.objects.get(tag=tag_name);
            note = Note(title = title, content = content, tag=tag);
            note.save();
            return redirect('index');
        
        tag = Tag(tag=tag_name);
        tag.save();
        note = Note(title = title, content = content, tag=tag);
        note.save();
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
    title = req.POST.get('titulo');
    note_req = req.GET.get('put')
    dict = {}
    print("______")
    print(req)
    print("______")
    for i in note_req.split('&'):
        k = i.split('=')[0]
        v = i.split('=')[1]
        dict[k] = v

    note = Note.objects.get(id=int(dict["id"]))
    tag = Tag.objects.get(tag=note.tag) 
    note.title = dict["title"]
    note.content = dict["content"]
    tag.tag = dict["tag"]
    tag.save()
    note.save()

    return redirect('index')

def get_tags(req):
    tags = Tag.objects.all()
    return render(req, 'notes/tags.html', {'tags': tags})

def get_postit_tags(req):
    tag_wanted = req.GET.get("tag")
    tag = Tag.objects.get(tag=tag_wanted)
    notes_wanted = Note.objects.filter(tag_id=tag.id)
    return render(req, 'notes/tag.html', {'notes': notes_wanted, 'tag': tag_wanted})