from django.shortcuts import render

from . import util
import random


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
    return render(request, "encyclopedia/create.html")

def rand(request):
    random_title = random.choice(util.list_entries())
    return render(request, "encyclopedia/entry.html", {
            "title": random_title,
            "entry_content": util.get_entry(random_title)
    })