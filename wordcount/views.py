from django.http import HttpResponse
from django.shortcuts import render
def homepage(request):
    return render("Hello django world!")
def here(request):
    return render("<h1>Dad I am here<h1>")
def wordcount(request):
    return render(request,'home.html')
def count(request):
    fulltext=request.GET['fulltext']
    wordlist=fulltext.split()
    return render(request,'count.html',{'fulltext':fulltext,'count':len(wordlist)})
