from django.http import HttpResponse
from django.shortcuts import render
from .models import SavedText

# Create your views here.
def SavedText_Create(request):
    return HttpResponse("<h1>Create</h1>")

def SavedText_List(request):
    queryset = SavedText.objects.all()
    context = {
        "objectList": queryset,
    }
    return render(request, "index.html", context)

def SavedText_Delete(request):
    return HttpResponse("<h1>Delete</h1>")
