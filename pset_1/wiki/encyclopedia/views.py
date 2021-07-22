from django.shortcuts import render
from django import forms
from . import util
import random, string
from django.utils.safestring import mark_safe

class CreateForm(forms.Form):
    titles = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Title'}))
    markdown = forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder': 'Please enter the markdown of encyclopdia.'}))

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "entry_content": util.get_entry(title)
    })

def search(request):
    title = request.POST.get('q')
    if title in util.list_entries():
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "entry_content": util.get_entry(title),
            "entry_list" : util.list_entries()
        })
    else:
        entries = []
        for e in util.list_entries():
            if title in e:
                entries.append(e)
        return render(request, "encyclopedia/search_result.html", {
            "entries": entries
        })

def create(request):
    if request.method == "POST":
        
    return render(request, "encyclopedia/create.html", {
        "form" : CreateForm()
    })

def rand(request):
    random_title = random.choice(util.list_entries())
    return render(request, "encyclopedia/entry.html", {
            "title": random_title,
            "entry_content": util.get_entry(random_title)
    })