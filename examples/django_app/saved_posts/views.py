from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import SavedText
from .forms import NotesForm

# Create your views here.
def SavedText_Create(request):
    form_class = NotesForm
    template_name = 'createNote.html'

    if request.POST:
        form = NotesForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            return redirect("/notebook/")
    else:
        form = NotesForm()

    return render(request, template_name, {'form': form})

def SavedText_List(request):
    queryset = SavedText.objects.all()
    context = {
        "objectList": queryset,
    }
    return render(request, "index.html", context)

def SavedText_Delete(request, id=None):
    instance = get_object_or_404(SavedText, id=id)
    instance.delete()
    messages.success(request, "Successfully Deleted")
    return redirect('/notebook')
