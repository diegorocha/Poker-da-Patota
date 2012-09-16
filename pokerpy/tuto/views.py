from django.shortcuts import render

def index(request):
    return render(request,'index.htm')

def maospoker(request):
    return render(request,'maosPoker.htm')

def regrasgerais(request):
    return render(request,'regrasGerais.html')