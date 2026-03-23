from django.shortcuts import render,redirect
from django.http import HttpResponse
from .form import NoteForm,MemoryForm
from .models import Note,Memory
from django.contrib import messages

# Create your views here.
# / → Home
def home(request):
    return render(request,'home.html')

# /notes/ → Notes section
def notes(request):
    notes=Note.objects.all()
    return render(request,'notes.html',{'notes':notes})

# /memories/ → Memories section
def memories(request):
    pics=Memory.objects.all()
    return render(request,'memories.html',{'pics':pics})

# /my-story/ → Your story section
def story(request):
    return render(request,'story.html')

def write_note(request):
    if request.method=='POST':
        form=NoteForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=NoteForm()
        
    return render(request,'write_note.html',{'form':form})
        
def upload_memory(request):
    if request.method == 'POST':
        form = MemoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Cloudinary handles the upload
            messages.success(request, "Memory uploaded successfully!")
            return redirect('upload_memory')
    else:
        form = MemoryForm()
    
    # Show all memories (optional)
    memories = Memory.objects.all().order_by('-uploaded_at')
    
    return render(request, 'upload_memory.html', {
        'form': form,
        'memories': memories
    })