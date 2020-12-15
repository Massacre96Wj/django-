from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def photo(request):
    return render(request, 'photo.html')

def xixi(request):
    return render(request, 'xixi.html')
