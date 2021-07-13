from django.shortcuts import render

def index(request):
    return render(request, 'coloring/index.html')

def ni(request):
    return render(request, 'coloring/new_interaction.html')