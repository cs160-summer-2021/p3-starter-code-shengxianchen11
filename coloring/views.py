from django.shortcuts import render

def index(request):
    return render(request, 'coloring/index.html')

def interaction(request):
    return render(request, 'coloring/new_interaction.html')

def triangle(request):
    return render(request, 'coloring/triangle_coloring.html')

def home(request):
    return render(request, 'coloring/home_page.html')

def cover(request):
    return render(request, 'coloring/cover.html')